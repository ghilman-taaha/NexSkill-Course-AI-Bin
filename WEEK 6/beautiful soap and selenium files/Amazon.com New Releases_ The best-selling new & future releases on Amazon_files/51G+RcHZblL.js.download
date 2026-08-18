////////////////////////////////////////////
;(function (packageFunction) {
  /* istanbul ignore next */
  var p = window.AmazonUIPageJS || window.P;
  /* istanbul ignore next */
  var attribute = p._namespace || p.attributeErrors;
  /* istanbul ignore next */
  var namespacedP = attribute ? attribute("IveAdaptiveVideosAsset", "") : p;

  /* istanbul ignore next */
  if (namespacedP.guardFatal) {
    namespacedP.guardFatal(packageFunction)(namespacedP, window);
  } else {
    namespacedP.execute(function () {
      packageFunction(namespacedP, window);
    });
  }
}(function(P, window, undefined){
// BEGIN ASSET IveAdaptiveVideosAsset - 2.0
/////////////////////////
// BEGIN FILE js/bundle.js
/////////////////////////
/*


Full source (including license, if applicable) included below.
*/
(function () {

    window.vseFeatures = window.vseFeatures || {};
    const gatedP = window.gatedP || {
        register: function (pFeatureFlag, globalFeatureFlag, action, promise, globalContext = window.vseFeatures) {
            P.now(pFeatureFlag).execute(pFeatureFlag + '-prereg', function (feature) {
                if (!feature && !globalContext[globalFeatureFlag]) {
                    globalContext[globalFeatureFlag] = true;
                    const result = promise.resolve(action(promise));
                    result.then(function () {
                        P.now(pFeatureFlag).execute(pFeatureFlag + '-reg', function (feature) {
                            if (!feature) {
                                P.log('Gated registration failed to register module!', 'ERROR', pFeatureFlag);
                                globalContext[globalFeatureFlag] = false;
                            }
                        });
                    });
                }
            });
        },
        declare: function (pFeatureFlag, globalFeatureFlag, value, globalContext = window.vseFeatures) {
            P.now(pFeatureFlag).execute(pFeatureFlag + '-prereg', function (feature) {
                if (!feature && !globalContext[globalFeatureFlag]) {
                    globalContext[globalFeatureFlag] = true;
                    P.declare(pFeatureFlag, value);
                }
            });
        }
    };

    /*
     * Copyright (c) 2019 Amazon.com, Inc. All rights reserved.
     */
    const auiUtils = {
        /**
         * Replace previous page state, which may be non-existent or old and stale (especially in case of Twister refresh)
         * with latest page state, parsed from DOM, and return it
         * @param A
         * @param pageStateName
         */
        fetchLatestPageState: (A, pageStateName) => {
            A.state.replace(pageStateName, JSON.parse(A.$(`script[type='a-state'][data-a-state*=${pageStateName}]`).html()));
            return A.state(pageStateName);
        },
        /**
         * checks undefined and null.
         * @param {object} obj
         * @returns {boolean} true if it is not undefined and null.
         */
        isDefined: (obj) => {
            return typeof obj !== "undefined" && obj !== null;
        },
    };

    /*
     * Copyright (c) 2018 Amazon.com, Inc. All rights reserved.
     */
    function emitDebugPayload(metricPayload) {
        if (!window.URLSearchParams) {
            return;
        }
        let urlParams = new window.URLSearchParams(window.location.search);
        if (urlParams.get('iveDebug') === '1') {
            if (window.DistributionMetricsDebugInfo) {
                window.DistributionMetricsDebugInfo.push(metricPayload);
            }
            else {
                window.DistributionMetricsDebugInfo = [metricPayload];
            }
        }
    }
    const postMetric = {
        count: function (metricName, value) {
            const ue = window.ue;
            if (ue) {
                metricName = `vse:csm:${metricName}`;
                ue.count(metricName, value);
            }
        },
        /**
        metricPayload structure should be : { events: [{data: metricsData}] }
        **/
        emitNexusMetric: function (metricPayload, producerId, schemaId, isInternal = false) {
            if (window.ue && window.ue.event && metricPayload && metricPayload.events && metricPayload.events[0] && metricPayload.events[0].data) {
                window.ue.event(metricPayload.events[0].data, producerId, schemaId);
                if (isInternal) {
                    emitDebugPayload(metricPayload.events[0].data);
                }
            }
        },
        emitSushiMetric: function (metricPayload, isInternal = false, sushiEndPoint, retryCount) {
            sushiEndPoint = sushiEndPoint || "https://unagi-na.amazon.com/1/events/com.amazon.eel.vse.metricstest.nexus";
            const retryLimit = 3;
            retryCount = retryCount || 0;
            if (retryCount >= retryLimit) {
                return;
            }
            /*
              remove '\' being added after stringify
              e.g. payload => {"json_payload":{"isMshop":false,"title":"some test title with "quote""}}
              JSON.stringify(payload) => {"json_payload":{"isMshop":false,"title":"some test title with \"quote\""}}
            */
            const sushiPayload = JSON.stringify(metricPayload).replace(/\\\\/g, "");
            const options = {
                params: sushiPayload,
                paramsFormat: 'json',
                contentType: 'application/json; charset=utf-8',
                error: () => {
                    this.emitSushiMetric(metricPayload, isInternal, sushiEndPoint, retryCount + 1);
                }
            };
            /*
              noted in https://sage.amazon.com/posts/468046, iOS ~11 and up, iOS is no longer
              granting apps certain permissions by default, so sendBeacon is restricted even
              though it is supported
            */
            const isIphone = navigator.userAgent.match(new RegExp('iPhone', 'i'));
            let isMshop = false;
            P.now('mash').execute('vse-detect-mshop', () => {
                isMshop = true;
            });
            const isIphoneMshop = (isIphone !== null) && isMshop;
            P.when('A').execute('Emit-VSE-Metrics', (A) => {
                if (navigator && navigator.sendBeacon && !isIphoneMshop) {
                    navigator.sendBeacon(sushiEndPoint, sushiPayload);
                }
                else {
                    A.post(sushiEndPoint, options);
                }
            });
            if (isInternal) {
                emitDebugPayload(metricPayload);
            }
        },
        logFatal: (attribution, message, exception) => {
            if (window.ueLogError) {
                const additionalInfo = {
                    logLevel: 'FATAL',
                    attribution: attribution,
                    message: message
                };
                window.ueLogError(exception, additionalInfo);
            }
        },
        logError: (attribution, message, exception) => {
            if (window.ueLogError) {
                const additionalInfo = {
                    logLevel: 'ERROR',
                    attribution: attribution,
                    message: message
                };
                window.ueLogError(exception, additionalInfo);
            }
        }
    };

    function guid() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    /*
     * Copyright (c) 2019 Amazon.com, Inc. All rights reserved.
     */
    const metricUtils = {
        /**
         * Utility for the first stage of universal Sushi reporting.  Makes an application-level function which can be used
         * to build sushi payloads for more granular event metrics
         * @param {AUIAStatic} A
         * @param {ISushiMetricsConfig} config
         * @returns {any} function accepting 'metricData' and returning a payload.  metricData is essentially a
         *                ISushiMetricsConfig where every parameter is optional.  If provided, will override defaults below
         */
        makeApplicationSushiPayloadBuilder: (A, config) => {
            return (metricData) => {
                let payloadTemplate = {
                    eventSource: config.eventSource,
                    requestId: config.requestId,
                    sessionId: config.sessionId,
                    placementContext: config.placementContext,
                    creativeId: config.creativeId || '', // Set for creative id from content symphony
                    marketplaceId: config.marketplaceId,
                    weblabIds: config.weblabIds,
                    clientId: config.clientId,
                    // downstream expects booleans to be strings
                    isInternal: config.isInternal.toString(),
                    isRobot: config.isRobot.toString(),
                    pageAsin: config.pageAsin,
                    customerId: config.customerId,
                    sessionType: config.sessionType || 1, // Dummy value unless overridden by caller
                    refMarkers: config.refMarkers,
                    eventId: guid(),
                    timestamp: new Date(),
                    userAgentData: navigator.userAgent,
                    titleSessionId: 0,
                    videoAsin: 0,
                    pageUrl: window.location.href !== null ? window.location.href.substring(0, 500) : '',
                    videoAsinList: config.videoAsinList || "",
                    rankingStrategy: ""
                };
                let payload = A.$.extend(payloadTemplate, metricData);
                const requestPayload = {
                    events: [{
                            data: payload,
                        }]
                };
                return requestPayload;
            };
        },
        makeApplicationNexusPayloadBuilder: (A, config) => {
            return (metricData) => {
                let payloadTemplate = {
                    eventSource: config.eventSource,
                    placementContext: config.placementContext,
                    userAgentData: navigator.userAgent,
                    videoAsin: config.videoAsin || "",
                    pageAsin: config.pageAsin || "",
                    videoAsinList: config.videoAsinList || "",
                    titleSessionId: "0",
                    stringPayload: "",
                    intPayload: 1,
                    rankingStrategy: "",
                    creativeId: config.creativeId || '', // Set for creative id from content symphony
                    clientId: config.clientId,
                    pageUrl: window.location.href !== null ? window.location.href.substring(0, 500) : '',
                    customerId: config.customerId || ''
                };
                return { events: [{ data: A.$.extend(payloadTemplate, metricData) }] };
            };
        },
        makeClickstreamNexusPayloadBuilder: (A, config) => {
            return (metricData) => {
                let payloadTemplate = {
                    timestamp: new Date(),
                    actionType: config.actionType,
                    eventOwner: config.producerId,
                    eventType: config.eventType,
                    productId: config.productId
                };
                return A.$.extend(payloadTemplate, metricData);
            };
        },
        extendWithNewField: (payloadTemplate, field, value) => {
            if (payloadTemplate && payloadTemplate.events && payloadTemplate.events[0] && payloadTemplate.events[0].data) {
                let data = payloadTemplate.events[0].data;
                data[field] = value;
                return {
                    events: [{
                            data: data
                        }]
                };
            }
            return payloadTemplate;
        },
    };

    /*
     * Copyright (c) 2019 Amazon.com, Inc. All rights reserved.
     */
    const ajaxRequestUtil = {
        sendRequest: (A, endpoint, payload, successCallback, errorCallback) => {
            A.ajax(endpoint, {
                params: payload,
                paramsFormat: 'json',
                crossDomain: true,
                method: 'POST',
                withCredentials: true,
                contentType: 'application/json',
                success: successCallback,
                error: errorCallback
            });
        }
    };

    const closedCaptionsUtils = {
        /**
         * Converts closed captions string (example: "en,https//:ccUrl.vtt") to the list
         * @param A AUI
         * @param closedCaptionsString closed captions string
         * @return collection of IClosedCaptions
         */
        getClosedCaptions: (A, closedCaptionsString) => {
            const closedCaptions = [];
            if (!A.objectIsEmpty(closedCaptionsString)) {
                const data = closedCaptionsString.split(',');
                for (let i = 0; i < data.length; i += 2) {
                    if (data[i + 1] !== undefined) {
                        closedCaptions.push({ locale: data[i], url: data[i + 1] });
                    }
                }
            }
            return closedCaptions;
        }
    };

    class DelphiAttribution {
        constructor(A) {
            this.A = A;
            this.buildTag = (config) => {
                if (!config.href)
                    return "";
                // vendor's OSP tracking ID
                let tag = "tag=" + config.vendorTrackingId;
                // product ASIN being attributed
                let asin = config.asin;
                if (!this.A.objectIsEmpty(asin)) {
                    asin = "&creativeASIN=" + asin;
                }
                // defaults to ive for now
                let link = "linkCode=";
                if (!this.A.objectIsEmpty(config.linkCode)) {
                    link += config.linkCode;
                }
                else {
                    link += "vse";
                }
                let aciContentId = config.aciContentId;
                let itemId = "";
                if (!this.A.objectIsEmpty(config.aciContentId)) {
                    itemId = "&asc_contentid=" + aciContentId;
                }
                let refParams = `${tag}&${link}${asin}${itemId}`;
                if (config.href.indexOf('?') < 0) {
                    refParams = `?${refParams}`;
                }
                else {
                    refParams = `&${refParams}`;
                }
                // build final url
                return config.href + refParams;
            };
        }
    }

    class Constants {
    }
    Constants.IVE_ADAPTIVE_METRICS_PREFIX = 'ive:aw';
    Constants.ATTRIBUTION_NAME = 'ive-adaptive-videos-asset';
    Constants.HAS_IVE_VIDEO = 'has-ive-video';
    Constants.HAS_WATCH_BUTTON = 'has-watch-button';
    Constants.DATA_ASIN_SELECTOR = '[data-asin]';
    Constants.ADAPTIVE_VIDEO_ELEMENT_SELECTOR = '[data-product-asin]';
    Constants.ASIN = 'asin';
    Constants.DATA_ASIN_ATTR = 'data-asin';
    Constants.ADAPTIVE_VIDEOS_UPDATE_ENDPOINT = '/vap/ew/adaptiveVideos/update';
    Constants.CANNOT_FIND_CLICKED_VIDEO = 'cannotFindClickedVideo';
    Constants.CANNOT_FIND_LB = 'cannotFindLightbox';
    Constants.CANNOT_FIND_PAGESTATE = 'cannotFindPageState';
    Constants.UPDATE_AJAX_FAILED = 'updateAjaxFailed';
    Constants.FALLBACK = 'fallback';
    Constants.WATCH_BUTTON_INGRESS_TYPE = 'watchButton';
    Constants.INLINE_WITH_WATCH_BUTTON_INGRESS_TYPE = 'inlineWithWatchButton';
    Constants.AW_WATCH_BUTTON_SELECTOR = '.ive-aw-watch-button';
    Constants.AW_WATCH_BUTTON_LABEL_SELECTOR = '.ive-aw-watch-button-label';
    Constants.ADDITIONAL_MAX_WIDTH_LABEL_SPACE = 11;
    Constants.EMPTY_STRING = "";
    Constants.METRIC_WIDGET_THUMBNAIL_RENDER = 'widget:thumbnail:render';
    Constants.METRIC_WIDGET_THUMBNAIL_CLICK = 'widget:thumbnail:click';
    Constants.METRIC_WIDGET_THUMBNAIL_IMPRESSION = 'widget:thumbnail:impression';
    Constants.METRIC_WIDGET_INLINE_PLAYBACK_CLICK = 'widget:inline:playback:click';
    Constants.PLAYER_WRAPPER_SELECTOR = '.ive-video-player-wrapper';
    Constants.INLINE_PLAYER_INGRESS_SELECTOR = '.ive-insitu-ingress-player-placeholder';
    Constants.VIDEO_PLAYING_CSS_CLASS = 'ive-video-playing';
    Constants.OSP_LINK_CSS_CLASS = 'ive-inline-player-osp-link';
    Constants.X_BUTTON_CSS_CLASS = 'ive-inline-player-close-button';
    Constants.AUDIO_TOGGLE_CSS_CLASS = 'ive-inline-player-audio-toggle';
    Constants.CLICK_ATTRIBUTION_INITIAL_DELAY_SEC = 2;
    Constants.INLINE_PLAYBACK_START = 'inlinePlaybackStart';

    class VideoItemIntersectionObserver {
        constructor(parent, childrenSelector, intersectingCallback, videoIsOutOfViewCallback, A) {
            this.addIntersectionObserverToNewPFO = (item) => {
                if (this.childElems.indexOf(item) !== -1)
                    return;
                this.intersectionInViewObserver.observe(item);
                this.intersectionOutOfViewObserver.observe(item);
                this.childElems.push(item);
            };
            this.onIntersectionObserved = (entries) => {
                for (let i = 0; i < entries.length; i++) {
                    const entry = entries[i];
                    const intersectingIndex = this.childElems.indexOf(entry.target);
                    if (entry.isIntersecting) {
                        this.intersectingCallback(intersectingIndex);
                    }
                }
            };
            this.onIntersectionOutOfViewObserved = (entries) => {
                for (let i = 0; i < entries.length; i++) {
                    const entry = entries[i];
                    if (!entry.isIntersecting && this.A.$(entry.target).hasClass(Constants.VIDEO_PLAYING_CSS_CLASS)) {
                        this.videoIsOutOfViewCallback();
                    }
                }
            };
            if (parent === undefined)
                parent = null;
            this.intersectingCallback = intersectingCallback;
            this.videoIsOutOfViewCallback = videoIsOutOfViewCallback;
            this.A = A;
            this.parentEle = parent;
            this.childElems = Array.prototype.slice.call(parent.querySelectorAll(childrenSelector)).filter((item) => {
                return item.classList.contains(Constants.HAS_IVE_VIDEO);
            });
            this.intersectionInViewObserver = new IntersectionObserver(this.onIntersectionObserved, {
                rootMargin: '0px',
                threshold: 0.85
            });
            this.intersectionOutOfViewObserver = new IntersectionObserver(this.onIntersectionOutOfViewObserved, {
                rootMargin: '0px',
                threshold: 0.05
            });
            this.childElems.forEach((item) => {
                this.intersectionInViewObserver.observe(item);
                this.intersectionOutOfViewObserver.observe(item);
            });
        }
    }

    class AdaptiveVideoWidget {
        constructor(A) {
            this.A = A;
            this.addVideoIngressAndMetricsHandlerForEligiblePFO = () => {
                var that = this;
                // using widgetSelector, find all elements where we can display video ingress
                // Add css class to show video ingress (play icon) to all elements that have videos
                this.vars.$widgetSelector.find(Constants.DATA_ASIN_SELECTOR).each(function () {
                    const $currentEl = that.vars.A.$(this);
                    const currentAssetSpec = that.vars.asinToVideoAssetSpec[$currentEl.attr(Constants.DATA_ASIN_ATTR)];
                    // 1) Newly added PFO has a video - adding video ingress
                    if (currentAssetSpec && !$currentEl.hasClass(Constants.HAS_IVE_VIDEO) && that.vars.videoIngressConfig.injectVideoIngress) {
                        that.addVideoIngress(this);
                        $currentEl.addClass(Constants.HAS_IVE_VIDEO);
                        if (that.vars.thumbnailIntersectionObserver && $currentEl[0]) {
                            that.vars.thumbnailIntersectionObserver.addIntersectionObserverToNewPFO($currentEl[0]);
                        }
                        // 2) We've already added video for this element in previous iteration (usually apears when de-selecting filter - do nothing)
                    }
                    else if (currentAssetSpec && $currentEl.hasClass(Constants.HAS_IVE_VIDEO)) {
                        return;
                        // 3) Newly added PFO doesn't have video
                    }
                    else if (that.vars.asinsWithoutVideo.indexOf($currentEl.attr(Constants.DATA_ASIN_ATTR)) === -1) {
                        that.vars.asinsWithoutVideo.push($currentEl.attr(Constants.DATA_ASIN_ATTR));
                        that.removeVideoIngress(this);
                        $currentEl.removeClass(Constants.HAS_IVE_VIDEO);
                        // 4) PFO was created by cloning PFO from another item with a video and new PFO doesn't have video
                    }
                    else {
                        that.removeVideoIngress(this);
                        $currentEl.removeClass(Constants.HAS_IVE_VIDEO);
                    }
                });
            };
            this.addVideoIngressClickHandler = () => {
                var that = this;
                this.vars.$widgetSelector.undelegate(this.vars.videoIngressPlaceholder, 'click touch');
                this.vars.$widgetSelector.delegate(this.vars.videoIngressPlaceholder, 'click touch', function (event) {
                    try {
                        // Don't open LB is player controls or osp link is clicked on inline player
                        if (that.isInlineVideo() && that.isPlayerOverlayElements(event.target)) {
                            return;
                        }
                        if (that.vars.clickedVideo) {
                            that.vars.previouslyClickedVideo = that.vars.clickedVideo;
                        }
                        const clickedAsin = that.vars.A.$(this).closest(Constants.DATA_ASIN_SELECTOR).attr(Constants.DATA_ASIN_ATTR);
                        that.vars.clickedVideo = that.vars.asinToVideoAssetSpec[clickedAsin];
                        if (!that.vars.clickedVideo) {
                            that.postCount(Constants.CANNOT_FIND_CLICKED_VIDEO);
                            that.vars.A.$(this).closest(Constants.DATA_ASIN_SELECTOR).removeClass(Constants.HAS_IVE_VIDEO);
                            return;
                        }
                        const modalFactory = that.getModalFactory();
                        that.vars.lightboxPopover = modalFactory && modalFactory.get(that.vars.A.$(`#${that.vars.popoverTriggerId}`));
                        if (that.vars.lightboxPopover) {
                            event.preventDefault();
                            event.stopPropagation();
                            that.movePlayerToLightbox();
                            that.vars.lightboxPopover.show();
                        }
                        else {
                            that.postCount(Constants.CANNOT_FIND_LB);
                            throw Error("Cannot find Lightbox for asin: " + clickedAsin);
                        }
                        that.emitNexusMetricWithProductAsin(`${that.vars.clientPrefix}:${Constants.METRIC_WIDGET_THUMBNAIL_CLICK}`, clickedAsin);
                    }
                    catch (exception) {
                        that.fallback(exception);
                    }
                });
            };
            this.addLightboxAfterShowAndBeforeHideEvents = () => {
                var that = this;
                // Bind Popover open event
                this.vars.A.off('a:popover:afterShow:' + this.vars.popoverId);
                this.vars.A.on('a:popover:afterShow:' + this.vars.popoverId, function vseVideosPopoverAfterShow(data) {
                    try {
                        let clickedAsin;
                        if (that.vars.lightboxOpenedFirstTime) {
                            // Apply IVE-specific classes to the top-level Popover element
                            const $popoverInner = that.vars.A.$(data.popover.$popover).find('[data-css-class]');
                            if ($popoverInner.length) {
                                that.vars.A.$(data.popover.$popover).addClass($popoverInner.attr('data-css-class'));
                            }
                            that.vars.lightboxOpenedFirstTime = false;
                            clickedAsin = that.vars.clickedVideo.productAsin;
                        }
                        else if (that.vars.clickedVideo.contentId !== that.vars.previouslyClickedVideo.contentId) {
                            clickedAsin = that.vars.clickedVideo.productAsin;
                        }
                        else {
                            // This means same product ingress opened again: we will not reload video carousel inside Lightbox
                            clickedAsin = undefined;
                        }
                        that.openLightbox(that.vars.clickedVideo, clickedAsin);
                    }
                    catch (exception) {
                        that.fallback(exception);
                    }
                });
                // Bind Popover close event
                this.vars.A.off('a:popover:beforeHide:' + this.vars.popoverId);
                this.vars.A.on('a:popover:beforeHide:' + this.vars.popoverId, function vseVideosPopoverBeforeHide() {
                    that.closeLightbox();
                });
            };
            this.openLightbox = (clickedVideo, clickedAsin) => {
                if (this.vars.widgetMutationObserver != null) {
                    this.vars.widgetMutationObserver.disconnect();
                }
                this.vars.lightboxOpened = true;
                this.vars.A.trigger(`vse:${this.vars.clientPrefix}:page:lightBoxOpened`, {
                    lightBoxId: this.vars.popoverId,
                    lazyLoadProductAsin: clickedAsin,
                    assetSpec: clickedVideo,
                    firstRelatedProductOverride: clickedAsin
                });
            };
            this.closeLightbox = () => {
                this.vars.A.trigger(`vse:${this.vars.clientPrefix}:page:lightBoxClosed`);
                this.movePlayerToIngress();
                this.vars.lightboxOpened = false;
                if (this.vars.widgetMutationObserver != null) {
                    this.startObservingWidget();
                }
            };
            this.addWidgetUpdateHandler = () => {
                var that = this;
                this.vars.A.off(`ive:${this.vars.clientPrefix}:adaptiveWidget:update`);
                this.vars.A.on(`ive:${this.vars.clientPrefix}:adaptiveWidget:update`, function adaptiveWidgetUpdate() {
                    let asinList = [];
                    that.vars.$widgetSelector.find(Constants.DATA_ASIN_SELECTOR).filter(function () {
                        const currentAsin = that.vars.A.$(this).attr(Constants.DATA_ASIN_ATTR);
                        if (that.isNewlyAddedAsin(currentAsin)) {
                            asinList.push(currentAsin);
                        }
                    });
                    if (asinList.length > 0) {
                        const request = {
                            asinList: asinList,
                            contentStrategy: that.vars.contentStrategy,
                            contentStrategyFilter: that.vars.contentStrategyFilter
                        };
                        const successCallback = function (result) {
                            if (result) {
                                let data = {};
                                data = that.convertToAdaptiveVideoAssetSpecList(result);
                                that.addDataToAsinToVideoAssetSpec(data);
                            }
                            that.addVideoIngressAndMetricsHandlerForEligiblePFO();
                        };
                        const errorCallback = function () {
                            that.postCount(Constants.UPDATE_AJAX_FAILED);
                        };
                        ajaxRequestUtil.sendRequest(that.vars.A, Constants.ADAPTIVE_VIDEOS_UPDATE_ENDPOINT, request, successCallback, errorCallback);
                    }
                    else {
                        that.addVideoIngressAndMetricsHandlerForEligiblePFO();
                    }
                });
                this.vars.A.off(`ive:${this.vars.clientPrefix}:adaptiveWidget:updateWithData`);
                this.vars.A.on(`ive:${this.vars.clientPrefix}:adaptiveWidget:updateWithData`, function adaptiveWidgetUpdateWithData() {
                    let asinToAdaptiveVideoElements = {};
                    that.vars.$widgetSelector.find(Constants.ADAPTIVE_VIDEO_ELEMENT_SELECTOR).filter(function () {
                        const currentAsin = that.vars.A.$(this).attr('data-product-asin');
                        if (that.isNewlyAddedAsin(currentAsin)) {
                            let adaptiveVideoElement = {
                                title: that.vars.A.$(this).attr('data-title'),
                                vendorName: that.vars.A.$(this).attr('data-vendor-name'),
                                contentId: that.vars.A.$(this).attr('data-content-id'),
                                videoUrl: that.vars.A.$(this).attr('data-video-url'),
                                productAsin: currentAsin,
                                groupType: that.vars.A.$(this).attr('data-group-type'),
                                videoHeight: that.vars.A.$(this).attr('data-video-height'),
                                videoWidth: that.vars.A.$(this).attr('data-video-width'),
                                imageUrl: "",
                                closedCaptions: closedCaptionsUtils.getClosedCaptions(that.vars.A, that.vars.A.$(this).attr('data-closed-captions')),
                                vendorTrackingId: that.vars.A.$(this).attr('data-vendor-tracking-id'),
                                videoReferenceId: that.vars.A.$(this).attr('data-video-reference-id'),
                                aciContentId: that.vars.A.$(this).attr('data-aci-content-id'),
                                profileUrl: that.vars.A.$(this).attr('data-profile-url'),
                                profileAvatarUrl: that.vars.A.$(this).attr('data-profile-avatar-url')
                            };
                            asinToAdaptiveVideoElements[currentAsin] = adaptiveVideoElement;
                        }
                    });
                    that.addDataToAsinToVideoAssetSpec(asinToAdaptiveVideoElements);
                    that.addVideoIngressAndMetricsHandlerForEligiblePFO();
                });
            };
            this.fallback = (exception) => {
                if (this.vars.$widgetSelector) {
                    this.vars.$widgetSelector.find(this.vars.videoIngressPlaceholder).hide();
                }
                if (this.vars.lightboxOpened && this.vars.lightboxPopover) {
                    this.vars.lightboxPopover.hide();
                    this.closeLightbox();
                }
                this.postCount(Constants.FALLBACK);
                postMetric.logError(Constants.ATTRIBUTION_NAME, `Fallback executed in IveAdaptiveVideosAsset for client ${this.vars.clientPrefix}`, exception);
            };
            this.addNexusMetricsConfigSetup = (config) => {
                if (config.nexusMetricsConfig) {
                    this.vars.nexusMetricsConfig = config.nexusMetricsConfig;
                    this.vars.buildNexusPayload = metricUtils.makeApplicationNexusPayloadBuilder(this.vars.A, this.vars.nexusMetricsConfig);
                    this.vars.emitNexusMetric = true;
                }
            };
            this.addImpressionMetricIntersectionObserver = (widgetSelector) => {
                this.vars.thumbnailIntersectionObserver = new VideoItemIntersectionObserver(document.querySelector(`${widgetSelector}`), `${Constants.DATA_ASIN_SELECTOR}, .${Constants.HAS_IVE_VIDEO}`, this.thumbnailImpressionsTrackerForMultipleImpressions, this.videoIsOutOfView, this.vars.A);
            };
            this.thumbnailImpressionsTrackerForMultipleImpressions = (index) => {
                this.vars.A.delay(() => {
                    const asinList = this.getAsinList();
                    if (!this.A.objectIsEmpty(asinList[index])) {
                        const asin = asinList[index].attr(Constants.DATA_ASIN_ATTR);
                        this.emitNexusMetricWithProductAsin(`${this.vars.clientPrefix}:${Constants.METRIC_WIDGET_THUMBNAIL_IMPRESSION}`, asin);
                    }
                }, 100);
            };
            this.isPlayerOverlayElements = (eventTarget) => {
                return this.vars.A.$(eventTarget).hasClass(Constants.OSP_LINK_CSS_CLASS)
                    || this.vars.A.$(eventTarget).hasClass(Constants.AUDIO_TOGGLE_CSS_CLASS)
                    || this.vars.A.$(eventTarget).hasClass(Constants.X_BUTTON_CSS_CLASS);
            };
            this.videoIsOutOfView = () => {
                if (this.isInlineVideo() && !this.vars.lightboxOpened) {
                    this.stopVideoAndReturnToPFO();
                }
            };
            this.convertToAdaptiveVideoAssetSpecList = (asinToVideoAssetSpec) => {
                let asinToVideoAsset = {};
                Object.keys(asinToVideoAssetSpec).forEach((asin, index) => {
                    asinToVideoAsset[asin] = {
                        title: asinToVideoAssetSpec[asin].title,
                        vendorName: asinToVideoAssetSpec[asin].vendorName,
                        contentId: asinToVideoAssetSpec[asin].asin,
                        videoUrl: asinToVideoAssetSpec[asin].videoURL,
                        productAsin: asin,
                        groupType: asinToVideoAssetSpec[asin].groupType,
                        relatedProducts: asin,
                        closedCaptions: closedCaptionsUtils.getClosedCaptions(this.vars.A, asinToVideoAssetSpec[asin].closedCaptions),
                        vendorTrackingId: asinToVideoAssetSpec[asin].vendorTrackingId,
                        videoReferenceId: asinToVideoAssetSpec[asin].referenceId,
                        aciContentId: asinToVideoAssetSpec[asin].aciContentId,
                        profileUrl: asinToVideoAssetSpec[asin].profileUrl,
                        profileAvatarUrl: asinToVideoAssetSpec[asin].profileAvatarUrl,
                        imageUrl: asinToVideoAssetSpec[asin].videoImage.url,
                        videoHeight: asinToVideoAssetSpec[asin].videoHeight,
                        videoWidth: asinToVideoAssetSpec[asin].videoWidth
                    };
                });
                return asinToVideoAsset;
            };
            this.addVideoIngress = (currentElement) => {
                // Inject play icon in the placeholder:
                let $watchButtonSelector;
                if (this.vars.videoIngressConfig.type === Constants.WATCH_BUTTON_INGRESS_TYPE) {
                    $watchButtonSelector = this.vars.A.$(currentElement).find(this.vars.videoIngressConfig.selector);
                }
                else if (this.vars.videoIngressConfig.type === Constants.INLINE_WITH_WATCH_BUTTON_INGRESS_TYPE) {
                    $watchButtonSelector = this.vars.A.$(currentElement).find(this.vars.videoIngressConfig.watchButtonSelector);
                    if (!this.vars.initializeInlinePlayerCalled) {
                        this.initializeInlinePlayer();
                        this.registerPageLevelOrchestrator();
                        this.vars.initializeInlinePlayerCalled = true;
                    }
                }
                this.addWatchButton($watchButtonSelector);
            };
            this.addWidgetMutationObserver = () => {
                const onWidgetUpdates = (mutationList) => {
                    for (const mutation of mutationList) {
                        if (mutation.addedNodes[0] instanceof HTMLElement &&
                            (mutation.addedNodes[0].dataset.asin || mutation.addedNodes[0].querySelector('[data-asin]'))) {
                            this.vars.A.trigger(`ive:${this.vars.clientPrefix}:adaptiveWidget:update`);
                            break;
                        }
                    }
                };
                this.vars.widgetMutationObserver = new MutationObserver(onWidgetUpdates);
                this.startObservingWidget();
            };
            this.startObservingWidget = () => {
                this.vars.widgetMutationObserver.observe(document.getElementById(this.vars.$widgetSelector.attr('id')), { childList: true, subtree: true });
            };
            /*
             * Setting max-width dynamically to account for different length of label text in different languages
             */
            this.addWatchButtonHoverHandler = (widgetHoverSelector) => {
                let that = this;
                let visibleLabelWidth = 0;
                const hoverSelector = widgetHoverSelector && widgetHoverSelector.trim() !== ""
                    ? widgetHoverSelector
                    : `.${Constants.HAS_IVE_VIDEO}`;
                this.vars.$widgetSelector.delegate(hoverSelector, 'mouseenter mouseleave', function (event) {
                    that.vars.A.$(this).toggleClass('ive-is-hovering', event.type === 'mouseenter');
                    const $awWatchButton = that.vars.A.$(this).find(Constants.AW_WATCH_BUTTON_SELECTOR);
                    let dynamicMaxWidth = parseInt($awWatchButton.css('max-width'), 10);
                    if (!that.vars.watchButtonInitialMaxWidth) {
                        that.vars.watchButtonInitialMaxWidth = dynamicMaxWidth;
                    }
                    if (visibleLabelWidth === 0) {
                        visibleLabelWidth = that.vars.A.$(this).find(Constants.AW_WATCH_BUTTON_LABEL_SELECTOR).width();
                    }
                    if (event.type === 'mouseenter') {
                        dynamicMaxWidth += visibleLabelWidth + Constants.ADDITIONAL_MAX_WIDTH_LABEL_SPACE;
                    }
                    else {
                        dynamicMaxWidth = that.vars.watchButtonInitialMaxWidth;
                    }
                    $awWatchButton.css({ 'max-width': dynamicMaxWidth + "px" });
                });
            };
            this.movePlayerToLightbox = () => {
                if (this.isInlineVideo()) {
                    this.vars.playerOptions.movePlayerToLightbox(this.vars.currentPFO.$videoContainer, this.vars.currentPFO.clickedAssetSpec);
                    this.togglePFOVisibility(true);
                }
            };
            this.movePlayerToIngress = () => {
                if (this.isInlineVideo()) {
                    this.stopVideoAndReturnToPFO();
                    this.resetWatchButtonWidth();
                    this.vars.currentPFO.$parentContainer.removeClass('ive-is-hovering');
                    setTimeout(() => this.vars.playerOptions.movePlayerToIngress(this.vars.currentPFO.$videoContainer), 50);
                }
            };
            this.removeVideoIngress = (currentElement) => {
                const $videoIngress = this.vars.A.$(currentElement).find(this.vars.videoIngressConfig.selector);
                $videoIngress.find(Constants.AW_WATCH_BUTTON_SELECTOR).css('display', 'none');
            };
            this.addWatchButton = ($videoIngress) => {
                const $awWatchButton = this.vars.$widgetSelector.find(Constants.AW_WATCH_BUTTON_SELECTOR);
                if ($awWatchButton && $awWatchButton.length > 0) {
                    $videoIngress
                        .removeClass('aok-hidden')
                        .html($awWatchButton.clone().removeClass('aok-hidden')[0].outerHTML)
                        .find(Constants.AW_WATCH_BUTTON_SELECTOR).animate({ opacity: 1 }, 300).css({ 'display': 'flex' });
                }
            };
            this.initializeInlinePlayer = () => {
                this.vars.A.on(`vse:ns:inlinePlayer:${this.vars.clientPrefix}:ready`, (playerOptions) => {
                    this.vars.player = playerOptions.playerInstance;
                    this.vars.playerOptions = playerOptions;
                    this.addInlinePlaybackClickHandler();
                    this.vars.player.on('playbackComplete', this.stopVideoAndReturnToPFO);
                    this.vars.A.on(`vse:ns:inlinePlayer:${this.vars.clientPrefix}:closeButton:click`, this.stopVideoAndReturnToPFO);
                    var that = this;
                    this.vars.player.on('timeupdate', function () {
                        const curTime = +that.vars.player.getCurrentTime().toFixed(0);
                        if (that.vars.currentPFO.videoWatchTracker.timestamps.indexOf(curTime) < 0) {
                            that.vars.currentPFO.videoWatchTracker.timestamps.push(curTime);
                        }
                        that.vars.currentPFO.videoWatchTracker.totalWatchDuration = that.vars.currentPFO.videoWatchTracker.timestamps.length;
                        if (that.isOspEnabledVideo(that.vars.currentPFO.clickedAssetSpec)
                            && that.vars.currentPFO.videoWatchTracker.isOspParamsAdded === false
                            && that.vars.currentPFO.videoWatchTracker.totalWatchDuration === Constants.CLICK_ATTRIBUTION_INITIAL_DELAY_SEC) {
                            that.updatePFOUrlWithOspAttribution();
                            that.vars.currentPFO.videoWatchTracker.isOspParamsAdded = true;
                        }
                    });
                });
            };
            this.registerPageLevelOrchestrator = () => {
                // Page-level event could be triggered from multiple Adaptive Video Widgets. Will pause any playing video in the current widget
                // if the widget is out of focus/hover
                this.vars.A.on(`ive:adaptiveWidget:videoStartPlaying`, () => {
                    if (this.vars.A.$(`${this.vars.widgetSelector}:hover`).size() === 0 && this.vars.A.$(`${this.vars.widgetSelector}:focus`).size() === 0
                        && this.vars.currentPFO.$parentContainer !== null) {
                        this.stopVideoAndReturnToPFO();
                        this.resetWatchButtonWidth();
                    }
                });
            };
            this.resetWatchButtonWidth = () => {
                if (!this.vars.A.capabilities.mobile) {
                    this.vars.currentPFO.$parentContainer
                        .find(Constants.AW_WATCH_BUTTON_SELECTOR)
                        .css({ 'max-width': this.vars.watchButtonInitialMaxWidth + 'px' });
                }
            };
            this.addInlinePlaybackClickHandler = () => {
                let that = this;
                let firstPlay = true;
                this.vars.$widgetSelector.undelegate(this.vars.videoIngressConfig.watchButtonSelector, 'click');
                this.vars.$widgetSelector.delegate(this.vars.videoIngressConfig.watchButtonSelector, 'click', function (event) {
                    try {
                        // Pause currently playing video
                        if (that.vars.currentPFO.$videoContainer && that.vars.currentPFO.$imageContainer) {
                            that.stopVideoAndReturnToPFO();
                        }
                        // Play newly clicked video
                        that.vars.currentPFO = {
                            watchButtonHtml: this,
                            $imageContainer: that.vars.A.$(event.target).closest(`.${Constants.HAS_IVE_VIDEO}`).find(that.vars.videoIngressConfig.pfoImageElementSelector),
                            $videoContainer: that.vars.$widgetSelector.find(Constants.INLINE_PLAYER_INGRESS_SELECTOR),
                            $parentContainer: that.vars.A.$(event.target).closest(`.${Constants.HAS_IVE_VIDEO}`),
                            videoWatchTracker: {
                                totalWatchDuration: 0,
                                timestamps: [],
                                isOspParamsAdded: false
                            }
                        };
                        // Save player's dom to the variable to reuse it when widget gets updated and player's dom is deleted
                        if (firstPlay) {
                            that.vars.currentPlayerContainer = that.vars.currentPFO.$videoContainer.detach().removeClass('aok-hidden');
                            firstPlay = false;
                        }
                        that.vars.currentPFO.$videoContainer = that.vars.currentPlayerContainer;
                        if (that.vars.currentPFO.$imageContainer.length > 0 && that.vars.currentPFO.$videoContainer.length > 0 && that.vars.player) {
                            that.togglePFOVisibility(false);
                            that.toggleWatchButtonVisibility(true);
                            that.toggleLinkOutline(that.vars.currentPFO.$imageContainer, true);
                            that.vars.currentPFO.$parentContainer.addClass(Constants.VIDEO_PLAYING_CSS_CLASS);
                            that.vars.currentPFO.$imageContainer.first().after(that.vars.currentPlayerContainer);
                            const clickedAsin = that.vars.A.$(this).closest(Constants.DATA_ASIN_SELECTOR).attr(Constants.DATA_ASIN_ATTR);
                            that.vars.currentPFO.clickedAssetSpec = that.vars.asinToVideoAssetSpec[clickedAsin];
                            that.vars.playerOptions.startPlaying(that.vars.currentPFO.clickedAssetSpec, that.vars.currentPFO.$videoContainer);
                            that.vars.A.trigger('ive:adaptiveWidget:videoStartPlaying');
                            that.emitNexusMetricWithProductAsin(that.vars.clientPrefix + ":" + Constants.METRIC_WIDGET_INLINE_PLAYBACK_CLICK, clickedAsin);
                        }
                        that.postCount(Constants.INLINE_PLAYBACK_START);
                    }
                    catch (exception) {
                        that.stopVideoAndReturnToPFO();
                        that.postCount(Constants.FALLBACK);
                    }
                });
            };
            this.stopVideoAndReturnToPFO = () => {
                this.vars.player.pause();
                this.togglePFOVisibility(true);
                this.toggleWatchButtonVisibility(false);
                this.toggleLinkOutline(this.vars.currentPFO.$imageContainer, false);
                this.vars.currentPFO.$parentContainer.removeClass(Constants.VIDEO_PLAYING_CSS_CLASS);
            };
            this.toggleLinkOutline = ($element, removeOutline) => {
                $element.closest('a').css({ 'outline': removeOutline ? 'none' : 'unset' });
            };
            this.toggleWatchButtonVisibility = (hideButton) => {
                this.vars.A.$(this.vars.currentPFO.watchButtonHtml).toggleClass('aok-hidden', hideButton);
            };
            this.togglePFOVisibility = (showImage) => {
                this.vars.currentPFO.$imageContainer.first().css({ 'visibility': showImage ? 'visible' : 'hidden' });
                this.vars.currentPFO.$videoContainer.first().css({ 'visibility': showImage ? 'hidden' : 'visible' });
            };
            this.isInlineVideo = () => {
                return this.vars.videoIngressConfig.type === Constants.INLINE_WITH_WATCH_BUTTON_INGRESS_TYPE;
            };
            this.getModalFactory = () => {
                let factory = null;
                if (this.vars.A.capabilities.mobile) {
                    P.now('a-secondary-view').execute('ive-aw-secondary-view-factory', function iveSecondaryViewFactory(modalFactory) {
                        factory = modalFactory;
                    });
                }
                else {
                    P.now('a-modal').execute('ive-aw-modal-factory', function iveModalFactory(modalFactory) {
                        factory = modalFactory;
                    });
                }
                return factory;
            };
            this.postCount = (metricName) => {
                postMetric.count(`${Constants.IVE_ADAPTIVE_METRICS_PREFIX}:${this.vars.clientPrefix}:${metricName}`, 1);
            };
            /**
             * emits metric.
             * @param metricName
             */
            this.emitNexusMetric = (metricName) => {
                if (this.vars.emitNexusMetric) {
                    const payload = this.vars.buildNexusPayload({
                        eventName: metricName,
                        stringPayload: Constants.EMPTY_STRING,
                        intPayload: 1
                    });
                    postMetric.emitNexusMetric(payload, this.vars.nexusMetricsConfig.producerId, this.vars.nexusMetricsConfig.widgetMetricsSchemaId, this.vars.nexusMetricsConfig.isInternal);
                }
            };
            /**
             * emits metric with productAsin in payload.
             * @param metricName
             * @param productAsin
             */
            this.emitNexusMetricWithProductAsin = (metricName, productAsin) => {
                if (this.vars.emitNexusMetric) {
                    const payload = this.vars.buildNexusPayload({
                        eventName: metricName,
                        stringPayload: Constants.EMPTY_STRING,
                        intPayload: 1,
                        productAsin: productAsin
                    });
                    postMetric.emitNexusMetric(payload, this.vars.nexusMetricsConfig.producerId, this.vars.nexusMetricsConfig.widgetMetricsSchemaId, this.vars.nexusMetricsConfig.isInternal);
                }
            };
            this.getAsinList = () => {
                let that = this;
                let asinList = [];
                this.vars.$widgetSelector.find(Constants.DATA_ASIN_SELECTOR).each(function () {
                    const $currentEl = that.vars.A.$(this);
                    if ($currentEl.hasClass(Constants.HAS_IVE_VIDEO) || $currentEl.find(`.${Constants.HAS_IVE_VIDEO}`).length > 0) {
                        asinList.push($currentEl);
                    }
                });
                return asinList;
            };
            this.isOspEnabledVideo = (assetSpec) => {
                return !this.vars.A.objectIsEmpty(assetSpec.vendorTrackingId) && assetSpec.vendorTrackingId !== '';
            };
            this.updatePFOUrlWithOspAttribution = () => {
                var that = this;
                // Parent PFO might have multiple DP urls (separate url for image, title and price)
                // Therefore, need to iterate over all urls in parent container which has /dp/ in href
                that.vars.currentPFO.$parentContainer.find('a[href*="/dp/"]').each(function () {
                    if (that.vars.A.$(this).attr('href').indexOf('linkCode') < 0) {
                        const hrefWithoutDelphiParams = that.vars.A.$(this).attr('href');
                        const attributionConfig = {
                            href: hrefWithoutDelphiParams,
                            asin: that.vars.currentPFO.clickedAssetSpec.productAsin,
                            linkCode: that.vars.ospLinkCode,
                            aciContentId: that.vars.currentPFO.clickedAssetSpec.aciContentId,
                            vendorTrackingId: that.vars.currentPFO.clickedAssetSpec.vendorTrackingId
                        };
                        const hrefWithDelphiParams = new DelphiAttribution(that.vars.A).buildTag(attributionConfig);
                        that.vars.A.$(this).attr('href', hrefWithDelphiParams);
                    }
                });
            };
            this.isNewlyAddedAsin = (asin) => {
                // find recently added elements to adaptive widget (not in asinsWithoutVideo and not in asinToVideoAssetSpec):
                return this.vars.asinsWithoutVideo.indexOf(asin) == -1 && !this.vars.asinToVideoAssetSpec[asin];
            };
            this.addDataToAsinToVideoAssetSpec = (data) => {
                if (Object.keys(this.vars.asinToVideoAssetSpec).length > 0) {
                    this.vars.asinToVideoAssetSpec = Object.assign({}, this.vars.asinToVideoAssetSpec, data);
                }
            };
            this.vars = {
                A: A,
                clientPrefix: '',
                $widgetSelector: null,
                emitNexusMetric: false,
                buildNexusPayload: '',
                nexusMetricsConfig: '',
                thumbnailIntersectionObserver: null,
                widgetMutationObserver: null,
                asinToVideoAssetSpec: null,
                videoIngressConfig: null,
                player: null,
                currentPFO: {
                    $imageContainer: null,
                    $videoContainer: null,
                    $parentContainer: null,
                    clickedAssetSpec: null,
                    watchButtonHtml: null
                },
                initializeInlinePlayerCalled: false,
                widgetSelector: null,
                lightboxPopover: null,
                contentStrategy: null,
                contentStrategyFilter: null,
                clickedVideo: null,
                previouslyClickedVideo: null,
                asinsWithoutVideo: [],
                videoIngressPlaceholder: null,
                popoverId: null,
                popoverTriggerId: null,
                lightboxOpened: false,
                lightboxOpenedFirstTime: true,
                watchButtonInitialMaxWidth: 0,
                ospLinkCode: ''
            };
        }
    }

    //Modules used only in aui unit tests
    const TestModules = {
        GatedP: gatedP,
        PostMetric: postMetric,
        AuiUtils: auiUtils,
        MetricUtils: metricUtils,
        DelphiAttribution: DelphiAttribution
    };

    try {
        const IveAdaptiveVideosAssetGatedRegistration = (promise) => {
            return new promise(function (resolve, reject) {
                P.when('A', 'ready').register('IveAdaptiveVideosAsset', function (A, promise) {
                    const initialize = (pageStateName) => {
                        let widget = new AdaptiveVideoWidget(A);
                        try {
                            const config = auiUtils.fetchLatestPageState(A, pageStateName);
                            if (!config) {
                                widget.postCount(Constants.CANNOT_FIND_PAGESTATE);
                                throw Error("Cannot find pagestate");
                            }
                            widget.vars.clientPrefix = config.clientPrefix;
                            widget.vars.ospLinkCode = config.ospLinkCode;
                            widget.vars.popoverId = config.lightboxPopoverConfig.popoverId;
                            widget.vars.popoverTriggerId = config.lightboxPopoverConfig.popoverTriggerId;
                            widget.vars.$widgetSelector = A.$(config.widgetSelector);
                            widget.vars.contentStrategy = config.contentStrategy;
                            widget.vars.contentStrategyFilter = config.contentStrategyFilter;
                            widget.vars.videoIngressConfig = config.videoIngressConfig;
                            widget.vars.videoIngressPlaceholder = widget.vars.videoIngressConfig.selector;
                            widget.vars.widgetSelector = config.widgetSelector;
                            widget.vars.asinToVideoAssetSpec = widget.convertToAdaptiveVideoAssetSpecList(config.asinToVideoAssetSpec);
                            widget.addVideoIngressAndMetricsHandlerForEligiblePFO();
                            widget.addVideoIngressClickHandler();
                            if (!A.capabilities.mobile) {
                                widget.addWatchButtonHoverHandler(config.widgetHoverSelector);
                            }
                            widget.addLightboxAfterShowAndBeforeHideEvents();
                            widget.addWidgetUpdateHandler();
                            widget.addNexusMetricsConfigSetup(config);
                            if (config.addWidgetMutationObserver === true) {
                                widget.addWidgetMutationObserver();
                            }
                            widget.addImpressionMetricIntersectionObserver(config.widgetSelector);
                            widget.emitNexusMetric(`${widget.vars.clientPrefix}:${Constants.METRIC_WIDGET_THUMBNAIL_RENDER}`);
                        }
                        catch (exception) {
                            widget.fallback(exception);
                        }
                    };
                    return {
                        initialize: initialize,
                        Utils: AdaptiveVideoWidget,
                        TestModules: TestModules,
                        _noneFeature: resolve()
                    };
                });
            });
        };
        P.when('A', '3p-promise').execute('IVE-gatedP-register-IveAdaptiveVideosAsset-client', (A, promise) => {
            gatedP.register('IveAdaptiveVideosAsset', 'IveAdaptiveVideosAsset-client-registered', IveAdaptiveVideosAssetGatedRegistration, promise);
        });
    }
    catch (exception) {
        postMetric.logError(Constants.ATTRIBUTION_NAME, 'Error during IveAdaptiveVideosAsset module registration', exception);
        postMetric.count(`${Constants.ATTRIBUTION_NAME}.moduleFatal`, 1);
    }

})();
/////////////////////////
// END FILE js/bundle.js
/////////////////////////
// END ASSET IveAdaptiveVideosAsset - 2.0
}));
////////////////////////////////////////////