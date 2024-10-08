sleektiv.define('iap.redirect_sleektiv_credit_widget', function(require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');


var IapSleektivCreditRedirect = AbstractAction.extend({
    template: 'iap.redirect_to_sleektiv_credit',
    events : {
        "click .redirect_confirm" : "sleektiv_redirect",
    },
    init: function (parent, action) {
        this._super(parent, action);
        this.url = action.params.url;
    },

    sleektiv_redirect: function () {
        window.open(this.url, '_blank');
        this.do_action({type: 'ir.actions.act_window_close'});
        // framework.redirect(this.url);
    },

});
core.action_registry.add('iap_sleektiv_credit_redirect', IapSleektivCreditRedirect);
});
