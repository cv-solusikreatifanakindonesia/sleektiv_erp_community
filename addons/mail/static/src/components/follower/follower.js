sleektiv.define('mail/static/src/components/follower/follower.js', function (require) {
'use strict';

const components = {
    FollowerSubtypeList: require('mail/static/src/components/follower_subtype_list/follower_subtype_list.js'),
};
const useShouldUpdateBasedOnProps = require('mail/static/src/component_hooks/use_should_update_based_on_props/use_should_update_based_on_props.js');
const useStore = require('mail/static/src/component_hooks/use_store/use_store.js');

const { markEventHandled } = require('mail/static/src/utils/utils.js');
const { Component } = owl;

class Follower extends Component {

    /**
     * @override
     */
    constructor(...args) {
        super(...args);
        useShouldUpdateBasedOnProps();
        useStore(props => {
            const follower = this.env.models['mail.follower'].get(props.followerLocalId);
            return [follower ? follower.__state : undefined];
        });
    }

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    /**
     * @returns {mail.follower}
     */
    get follower() {
        return this.env.models['mail.follower'].get(this.props.followerLocalId);
    }

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     * @param {MouseEvent} ev
     */
    _onClickDetails(ev) {
        ev.preventDefault();
        ev.stopPropagation();
        this.follower.openProfile();
    }

    /**
     * @private
     * @param {MouseEvent} ev
     */
    _onClickEdit(ev) {
        ev.preventDefault();
        this.follower.showSubtypes();
    }

    /**
     * @private
     * @param {MouseEvent} ev
     */
    async _onClickRemove(ev) {
        markEventHandled(ev, 'Follower.clickRemove');
        await this.follower.remove();
        this.trigger('reload', { fieldNames:['message_follower_ids'], keepChanges: true });
        this.trigger('o-hide-follower-list-menu');
    }

}

Object.assign(Follower, {
    components,
    props: {
        followerLocalId: String,
    },
    template: 'mail.Follower',
});

return Follower;

});
