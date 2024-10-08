sleektiv.define("website.tour.snippet_image_gallery", function (require) {
"use strict";

const tour = require("web_tour.tour");
const wTourUtils = require("website.tour_utils");

tour.register("snippet_image_gallery", {
    test: true,
    url: "/",
}, [
    ...wTourUtils.clickOnEditAndWaitEditMode(),
    wTourUtils.dragNDrop({
        id: "s_image_gallery",
        name: "Image Gallery",
}), {
    content: "Click on the first new image",
    trigger: ".o_select_media_dialog img[title='s_default_image.jpg']",
}, {
    content: "Click on the second new image",
    trigger: ".o_select_media_dialog img[title='s_default_image2.jpg']",
}, {
    content: "Click on Add",
    trigger: "button:has(span:contains('Add'))",
}, {
    content: "Click on the image of the Image Gallery snippet",
    trigger: ".s_image_gallery .carousel-item.active  img",
}, {
    content: "Click on Remove Block",
    trigger: ".o_we_customize_panel we-title:has(span:contains('Image Gallery')) we-button[title='Remove Block']",
}, {
    content: "Check that the Image Gallery snippet has been removed",
    trigger: "#wrap:not(:has(.s_image_gallery))",
    run: () => null,
}]);
});
