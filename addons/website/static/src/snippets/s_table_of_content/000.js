sleektiv.define('website.s_table_of_content', function (require) {
'use strict';

const publicWidget = require('web.public.widget');
const {extraMenuUpdateCallbacks} = require('website.content.menu');

const TableOfContent = publicWidget.Widget.extend({
    selector: 'section .s_table_of_content_navbar_sticky',
    disabledInEditableMode: false,

    /**
     * @override
     */
    async start() {
        await this._super(...arguments);
        this.$scrollingElement = this.$target.closest(".s_table_of_content").closestScrollable();
        this.previousPosition = -1;
        this._updateTableOfContentNavbarPosition();

        this.boundUpdateNavbar = this._updateTableOfContentNavbarPosition.bind(this);
        extraMenuUpdateCallbacks.push(this.boundUpdateNavbar);
    },
    /**
     * @override
     */
    destroy() {
        const indexOfCallback = extraMenuUpdateCallbacks.indexOf(this.boundUpdateNavbar);
        extraMenuUpdateCallbacks.splice(indexOfCallback, 1);
        this.$target.css('top', '');
        this.$target.find('.s_table_of_content_navbar').css({top: '', maxHeight: ''});
        this._super(...arguments);
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _updateTableOfContentNavbarPosition() {
        let position = 0;
        const $fixedElements = $('.o_top_fixed_element');
        _.each($fixedElements, el => position += $(el).outerHeight());
        const isHorizontalNavbar = this.$target.hasClass('s_table_of_content_horizontal_navbar');
        this.$target.css('top', isHorizontalNavbar ? position : '');
        this.$target.find('.s_table_of_content_navbar').css('top', isHorizontalNavbar ? '' : position + 20);
        const $mainNavBar = $('#oe_main_menu_navbar');
        const mainNavBarHidden = document.body.classList.contains('o_fullscreen') || this.editableMode;
        position += !mainNavBarHidden && $mainNavBar.length ? $mainNavBar.outerHeight() : 0;
        position += isHorizontalNavbar ? this.$target.outerHeight() : 0;
        this.$target.find('.s_table_of_content_navbar').css('maxHeight', isHorizontalNavbar ? '' : `calc(100vh - ${position + 40}px)`);
        if (this.previousPosition !== position) {
            // The scrollSpy must be destroyed before calling it again.
            // Otherwise the call has no effect. We also need to be sure that
            // a scrollSpy instance exists to avoid targeting elements outside
            // the table of content navbar on scrollSpy methods.
            if (this.$scrollingElement.data('bs.scrollspy')) {
                this.$scrollingElement.scrollspy('dispose');
            }
            this.$scrollingElement.scrollspy({
                target: '.s_table_of_content_navbar',
                method: 'offset',
                offset: position + 100,
                alwaysKeepFirstActive: true,
            });
            this.previousPosition = position;
        }
    },
});

publicWidget.registry.anchorSlide.include({

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * Overridden to add the height of the horizontal sticky navbar at the scroll value
     * when the link is from the table of content navbar
     *
     * @override
     * @private
     */
    _computeExtraOffset() {
        let extraOffset = this._super(...arguments);
        if (this.$el.hasClass('table_of_content_link')) {
            const tableOfContentNavbarEl = this.$el.closest('.s_table_of_content_navbar_sticky.s_table_of_content_horizontal_navbar');
            if (tableOfContentNavbarEl.length > 0) {
                extraOffset += $(tableOfContentNavbarEl).outerHeight();
            }
        }
        return extraOffset;
    },
});

publicWidget.registry.snippetTableOfContent = TableOfContent;

return TableOfContent;
});
