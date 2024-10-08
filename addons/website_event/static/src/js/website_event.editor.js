sleektiv.define('website_event.editor', function (require) {
"use strict";

var core = require('web.core');
var wUtils = require('website.utils');
var WebsiteNewMenu = require('website.newMenu');

var _t = core._t;

WebsiteNewMenu.include({
    actions: _.extend({}, WebsiteNewMenu.prototype.actions || {}, {
        new_event: '_createNewEvent',
    }),

    //--------------------------------------------------------------------------
    // Actions
    //--------------------------------------------------------------------------

    /**
     * Asks the user information about a new event to create, then creates it
     * and redirects the user to this new event.
     *
     * @private
     * @returns {Promise} Unresolved if there is a redirection
     */
    _createNewEvent: function () {
        var self = this;
        return wUtils.prompt({
            id: "editor_new_event",
            window_title: _t("New Event"),
            input: _t("Event Name"),
        }).then(function (result) {
            var eventName = result.val;
            if (!eventName) {
                return;
            }
            return self._rpc({
                route: '/event/add_event',
                params: {
                    event_name: eventName,
                },
            }).then(function (url) {
                window.location.href = url;
                return new Promise(function () {});
            });
        });
    },
});
});
