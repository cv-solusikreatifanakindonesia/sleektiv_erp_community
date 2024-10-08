sleektiv.define('point_of_sale.tour.ReceiptScreenTourMethods', function (require) {
    'use strict';

    const { createTourMethods } = require('point_of_sale.tour.utils');

    class Do {
        clickNextOrder() {
            return [
                {
                    content: 'go to next screen',
                    trigger: '.receipt-screen .button.next.highlight',
                },
            ];
        }
        setEmail(email) {
            return [
                {
                    trigger: '.receipt-screen .input-email input',
                    run: `text ${email}`,
                },
            ];
        }
        clickSend(isHighlighted = true) {
            return [
                {
                    trigger: `.receipt-screen .input-email .send${isHighlighted ? '.highlight' : ''}`,
                },
            ];
        }
    }

    class Check {
        isShown() {
            return [
                {
                    content: 'receipt screen is shown',
                    trigger: '.pos .receipt-screen',
                    run: () => {},
                },
            ];
        }

        receiptIsThere() {
            return [
                {
                    content: 'there should be the receipt',
                    trigger: '.receipt-screen .pos-receipt',
                    run: () => {},
                },
            ];
        }

        totalAmountContains(value) {
            return [
                {
                    trigger: `.receipt-screen .top-content h1:contains("${value}")`,
                    run: () => {},
                },
            ];
        }

        emailIsSuccessful() {
            return [
                {
                    trigger: `.receipt-screen .notice.successful`,
                    run: () => {},
                },
            ];
        }
        discountAmountIs(value) {
            return [
                {
                    trigger: `.pos-receipt>div:contains("Discounts")>span:contains("${value}")`,
                    run: () => {},
                },
            ];
        }
    }

    class Execute {
        nextOrder() {
            return [...this._check.isShown(), ...this._do.clickNextOrder()];
        }
    }

    return createTourMethods('ReceiptScreen', Do, Check, Execute);
});
