import os
import time
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

BUFFER_SIZE = 53940
BATCH_SIZE = 256
DATA_DIM = 7
Z_DIM = 100
EPOCHS = 50
SAVE_EVERY = 5
GENERATOR_LR = 2e-4
DISCRIMINATOR_LR = 2e-4
BETA_1 = 0.5
OUTPUT_DIR = "generated_images"
MODEL_DIR = "models"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# data, 7 numeric columns scaled to -1 and 1
features = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
diamonds_data = pd.read_csv(r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', index_col='Unnamed: 0')
real_sample = diamonds_data[features].sample(2000, random_state=42).values

scaler = MinMaxScaler(feature_range=(-1, 1))
x_train = scaler.fit_transform(diamonds_data[features].values).astype('float32')

dataset = tf.data.Dataset.from_tensor_slices(x_train)
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

# generator
def build_generator(z_dim=Z_DIM):
    model = keras.Sequential(name="generator")
    model.add(layers.Dense(256, use_bias=False, input_shape=(z_dim,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(128, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(64, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(DATA_DIM, activation='tanh'))
    return model

# discriminator
def build_discriminator(data_dim=DATA_DIM):
    model = keras.Sequential(name="discriminator")
    model.add(layers.Dense(128, input_shape=(data_dim,)))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Dense(64))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Dense(1))
    return model

generator = build_generator()
discriminator = build_discriminator()

# losses
cross_entropy = keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_output, fake_output):
    real_labels = tf.ones_like(real_output)
    fake_labels = tf.zeros_like(fake_output)
    real_loss = cross_entropy(real_labels, real_output)
    fake_loss = cross_entropy(fake_labels, fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

def generator_loss(fake_output):
    fool_labels = tf.ones_like(fake_output)
    return cross_entropy(fool_labels, fake_output)

generator_optimizer = keras.optimizers.Adam(learning_rate=GENERATOR_LR, beta_1=BETA_1)
discriminator_optimizer = keras.optimizers.Adam(learning_rate=DISCRIMINATOR_LR, beta_1=BETA_1)

checkpoint_prefix = os.path.join(MODEL_DIR, "ckpt")
checkpoint = tf.train.Checkpoint(generator_optimizer=generator_optimizer,
                                 discriminator_optimizer=discriminator_optimizer,
                                 generator=generator,
                                 discriminator=discriminator)

# save plot, real vs generated diamonds
fixed_seed = tf.random.normal([2000, Z_DIM])

def save_generated_images(model, epoch, test_input=fixed_seed):
    predictions = model(test_input, training=False)
    predictions = scaler.inverse_transform(predictions.numpy())

    fig = plt.figure(figsize=(6,5))
    plt.scatter(real_sample[:, 0], real_sample[:, 3], s=3, alpha=0.4, label='Real')
    plt.scatter(predictions[:, 0], predictions[:, 3], s=3, alpha=0.4, label='Generated')
    plt.xlabel('carat')
    plt.ylabel('price')
    plt.legend()

    plt.suptitle(f'Epoch {epoch}')
    filename = os.path.join(OUTPUT_DIR, f'generated_epoch_{str(epoch).zfill(3)}.png')
    plt.savefig(filename)
    plt.close(fig)

@tf.function
def train_step(images):
    batch_size = tf.shape(images)[0]
    noise = tf.random.normal([batch_size, Z_DIM])

    with tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

    noise = tf.random.normal([batch_size, Z_DIM])
    with tf.GradientTape() as gen_tape:
        generated_images = generator(noise, training=True)
        fake_output = discriminator(generated_images, training=True)
        gen_loss = generator_loss(fake_output)

    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))

    return gen_loss, disc_loss

def train(dataset, epochs):
    print("Starting training...")
    for epoch in range(1, epochs + 1):
        start = time.time()
        gen_loss_avg = keras.metrics.Mean()
        disc_loss_avg = keras.metrics.Mean()

        for image_batch in dataset:
            g_loss, d_loss = train_step(image_batch)
            gen_loss_avg.update_state(g_loss)
            disc_loss_avg.update_state(d_loss)

        if epoch % SAVE_EVERY == 0 or epoch == 1:
            save_generated_images(generator, epoch)
            checkpoint.save(file_prefix=checkpoint_prefix)

        print(f'Epoch {epoch}, Gen Loss: {gen_loss_avg.result():.4f}, Disc Loss: {disc_loss_avg.result():.4f}, Time: {time.time()-start:.2f}s')

    generator.save(os.path.join(MODEL_DIR, 'generator_final.h5'))
    discriminator.save(os.path.join(MODEL_DIR, 'discriminator_final.h5'))

if __name__ == '__main__':
    tf.random.set_seed(42)
    np.random.seed(42)

    train(dataset, EPOCHS)

    save_generated_images(generator, 'final')

    print(pd.DataFrame(scaler.inverse_transform(generator(fixed_seed[:5], training=False).numpy()), columns=features))

    print('Training complete. Generated images in', OUTPUT_DIR)