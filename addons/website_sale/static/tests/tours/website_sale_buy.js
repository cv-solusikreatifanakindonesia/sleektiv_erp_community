sleektiv.define('website_sale.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('shop_buy_product', {
    test: true,
    url: '/shop',
},
    [
        {
            content: "search conference chair",
            trigger: 'form input[name="search"]',
            run: "text conference chair",
        },
        {
            content: "search conference chair",
            trigger: 'form:has(input[name="search"]) .oe_search_button',
        },
        {
            content: "select conference chair",
            trigger: '.oe_product_cart:first a:contains("Conference Chair")',
        },
        {
            content: "select Conference Chair Aluminium",
            extra_trigger: '#product_detail',
            trigger: 'label:contains(Aluminium) input',
        },
        {
            content: "select Conference Chair Steel",
            extra_trigger: '#product_detail',
            trigger: 'label:contains(Steel) input',
        },
        {
            id: 'add_cart_step',
            content: "click on add to cart",
            extra_trigger: 'label:contains(Steel) input:propChecked',
            trigger: '#product_detail form[action^="/shop/cart/update"] .btn-primary',
        },
        {
            content: "add suggested",
            extra_trigger: '#wrap:not(:has(#cart_products:contains("Storage Box")))',
            trigger: '.oe_cart:has(tr:contains("Storage Box")) a:contains("Add to Cart")',
        },
        {
            content: "add one more",
            extra_trigger: '#cart_products tr:contains("Storage Box")',
            trigger: '#cart_products tr:contains("Steel") a.js_add_cart_json:eq(1)',
        },
        {
            content: "remove Storage Box",
            extra_trigger: '#cart_products tr:contains("Steel") input.js_quantity:propValue(2)',
            trigger: '#cart_products tr:contains("Storage Box") a.js_add_cart_json:first',
        },
        {
            content: "set three",
            extra_trigger: '#wrap:not(:has(#cart_products tr:contains("Storage Box")))',
            trigger: '#cart_products input.js_quantity',
            run: 'text 3',
        },
        {
            content: "check amount",
            // wait for cart_update_json to prevent concurrent update
            trigger: '#order_total span.oe_currency_value:contains("49.50")',
            run: function () {}, // it's a check
        },
        {
            content: "go to checkout",
            extra_trigger: '#cart_products input.js_quantity:propValue(3)',
            trigger: 'a[href*="/shop/checkout"]',
        },
        {
            content: "select payment",
            trigger: '#payment_method label:contains("Wire Transfer")',
        },
        {
            content: "Pay Now",
            //Either there are multiple payment methods, and one is checked, either there is only one, and therefore there are no radio inputs
            extra_trigger: '#payment_method label:contains("Wire Transfer") input:checked,#payment_method:not(:has("input:radio:visible"))',
            trigger: 'button[id="o_payment_form_pay"]:visible:not(:disabled)',
        },
        {
            content: "finish",
            trigger: '.oe_website_sale:contains("Please make a payment to:")',
            // Leave /shop/confirmation to prevent RPC loop to /shop/payment/get_status.
            // The RPC could be handled in python while the tour is killed (and the session), leading to crashes
            run: function () {
                window.location.href = '/contactus'; // Redirect in JS to avoid the RPC loop (20x1sec)
            },
            timeout: 30000,
        },
        {
            content: "wait page loaded",
            trigger: 'h1:contains("Contact us")',
            run: function () {}, // it's a check
        },
    ]
);

});
