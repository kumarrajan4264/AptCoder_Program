
  var packageTabs = document.querySelectorAll('.tab[data-pricing-plan]');
  var packageTabsContext = document.querySelectorAll('.curriculum__pricing_tab_context[data-pricing-plan]');

  if (packageTabs.length) {
    for (var i = 0; i < packageTabs.length; i++) {
      packageTabs[i].classList.remove('active');
      packageTabsContext[i].classList.add('hide');
    }
    packageTabs[0].classList.add('active');
    packageTabsContext[0].classList.remove('hide');
  }

  for (var i = 0; i < packageTabs.length; i++) {
    packageTabs[i].addEventListener('click', function (e) {
      tabChange(this.dataset.pricingPlan, false);
    })
  }

  function tabChange(planId, scrollToSection) {
    scrollToSection = scrollToSection !== false;
    var packageTabs = document.querySelectorAll('.tab[data-pricing-plan]');
    var packageTabsContext = document.querySelectorAll('.curriculum__pricing_tab_context[data-pricing-plan]');
    for (var i = 0; i < packageTabs.length; i++) {
      packageTabs[i].classList.remove('active');
      packageTabsContext[i].classList.add('hide');
    }
    document.querySelector('.tab[data-pricing-plan=' + planId + ']').classList.add('active');
    document.querySelector('.curriculum__pricing_tab_context[data-pricing-plan=' + planId + ']').classList.remove('hide');
    if(scrollToSection){
      document.getElementById('curriculum-section').scrollIntoView();
    }
  }

   window.addEventListener('DOMContentLoaded', function (event) {
    var sectionTargets = document.querySelectorAll("section") || [];
    var barChartTarget = document.querySelector('.why-coding__bars');
    var countTarget = document.getElementById('teacher-info-section');

    try {
      var callback = function (entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible-viewport");
          }
        });
      };

      // start section anime


      var observer = new IntersectionObserver(callback, {
        threshold: 0.1
      });

      for (var i = 0; i < sectionTargets.length; i++) {
        observer.observe(sectionTargets[i]);
      }

      // end section anime

      // start barchart anime


      var barObserver = new IntersectionObserver(callback, {
        threshold: 1
      });

      barObserver.observe(barChartTarget)

      // end barchart anime

      // start count anime


      var countObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var counters = document.querySelectorAll('.counter');
            var speed = 100;

            counters.forEach(function (counter) {
              var updateCount = function () {
                var target = +counter.getAttribute('data-target');
                var count = +counter.innerText;

                var inc = target / speed;
                if (count < target) {
                  counter.innerText = count + inc;
                  setTimeout(updateCount, 1);
                } else {
                  counter.innerText = target.toLocaleString();
                }
              };
              updateCount();
            });
          }
        });
      }, {
        threshold: 1
      });

      countObserver.observe(countTarget)

      // end count anime
    } catch (e) {
      // on intersection observer not available
      for (var i = 0; i < sectionTargets.length; i++) {
        sectionTargets[i].classList.add("is-visible-viewport");
      }

      barChartTarget.classList.add('is-visible-viewport')
    }
  });


  window.addEventListener('DOMContentLoaded', function (event) {
    var sectionTargets = document.querySelectorAll("section") || [];
    var barChartTarget = document.querySelector('.why-coding__bars');
    var countTarget = document.getElementById('teacher-info-section');

    try {
      var callback = function (entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible-viewport");
          }
        });
      };

      // start section anime


      var observer = new IntersectionObserver(callback, {
        threshold: 0.1
      });

      for (var i = 0; i < sectionTargets.length; i++) {
        observer.observe(sectionTargets[i]);
      }

      // end section anime

      // start barchart anime


      var barObserver = new IntersectionObserver(callback, {
        threshold: 1
      });

      barObserver.observe(barChartTarget)

      // end barchart anime

      // start count anime


      var countObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var counters = document.querySelectorAll('.counter');
            var speed = 100;

            counters.forEach(function (counter) {
              var updateCount = function () {
                var target = +counter.getAttribute('data-target');
                var count = +counter.innerText;

                var inc = target / speed;
                if (count < target) {
                  counter.innerText = count + inc;
                  setTimeout(updateCount, 1);
                } else {
                  counter.innerText = target.toLocaleString();
                }
              };
              updateCount();
            });
          }
        });
      }, {
        threshold: 1
      });

      countObserver.observe(countTarget)

      // end count anime
    } catch (e) {
      // on intersection observer not available
      for (var i = 0; i < sectionTargets.length; i++) {
        sectionTargets[i].classList.add("is-visible-viewport");
      }

      barChartTarget.classList.add('is-visible-viewport')
    }
  });
