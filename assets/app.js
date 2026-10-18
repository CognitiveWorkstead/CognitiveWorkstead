(function () {
  const toggle = document.querySelector("[data-menu-toggle]");
  const nav = document.querySelector("[data-primary-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      nav.classList.toggle("is-open", !expanded);
    });
  }

  const path = window.location.pathname.replace(/\/index\.html$/, "/");
  document.querySelectorAll("[data-nav-link]").forEach((link) => {
    const href = link.getAttribute("href") || "";
    const normalized = new URL(href, window.location.href).pathname.replace(/\/index\.html$/, "/");
    if (normalized === path) {
      link.setAttribute("aria-current", "page");
    }
  });

  const assessmentForm = document.querySelector("#assessment-form");
  const result = document.querySelector("#assessment-result");
  if (assessmentForm && result) {
    assessmentForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const checked = assessmentForm.querySelectorAll("[data-assessment-item]:checked").length;
      let title = "Start with discovery.";
      let body = "Your best next step is to clarify the workflow, owner, examples, data boundaries, and review model before choosing a pilot.";
      if (checked >= 5) {
        title = "You are ready to plan a pilot.";
        body = "You have enough signal for a bounded AI pilot. Pick one workflow, define a human review loop, and choose one success measure.";
      } else if (checked >= 3) {
        title = "You have a workable starting point.";
        body = "There is likely a practical first project here. Tighten the workflow scope, gather examples, and decide what humans must review.";
      }
      result.innerHTML = `<span class="badge">Result: ${checked}/6</span><h3>${title}</h3><p>${body}</p><div class="cta-row"><a class="button ghost" href="../contact/">Start a Conversation</a></div>`;
    });
  }
})();
