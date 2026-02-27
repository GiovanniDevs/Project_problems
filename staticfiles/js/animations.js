/*
  animations.js

  GSAP-based UI animations for the site hero section. Loaded on
  `DOMContentLoaded` so animations run once the DOM is ready.

  - Background subtle zoom: `.hero-img`
  - Staggered text reveals: `.hero-title-1`, `.hero-title-2`, `.hero-lead`

  Requires GSAP (gsap.min.js) to be included before this script.
*/

document.addEventListener("DOMContentLoaded", function () {
  // 1️⃣ Background subtle zoom
  gsap.from(".hero-img", {
    scale: 1.1,
    duration: 1.5,
    ease: "power2.out",
  });

  // 2️⃣ Animate text in sequence
  gsap.from(".hero-title-1", {
    y: 40,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out",
  });

  gsap.from(".hero-title-2", {
    y: 40,
    opacity: 0,
    duration: 0.8,
    delay: 0.4,
    ease: "power3.out",
  });

  gsap.from(".hero-lead", {
    y: 30,
    opacity: 0,
    duration: 0.8,
    delay: 0.8,
    ease: "power3.out",
  });
});
