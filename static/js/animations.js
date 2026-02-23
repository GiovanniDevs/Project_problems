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
