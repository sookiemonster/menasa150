// Aggregate timeline variables
let timeline_sections = document.querySelectorAll('.section-header');
let timeline_events = document.querySelectorAll('.event-container');

let sectionIdPrefix = "timeline-section";

/**
 * Remove '.active' from all timeline elements
 */
let clear_active = () => {
   for (i = 0; i < timeline_events.length; i++) {
      timeline_events[i].classList.remove('active');
   }  
   for (i = 0; i < timeline_sections.length; i++) {
      timeline_sections[i].classList.remove('active');
   }
}

let highlightElement = (target) => {
   target.classList.add('active');
}

let highlightParentSection = (target) => {
   if (target.classList.contains('event-container')) {
      let sectionNumber = target.closest(".event-list").dataset.sectionNo;
      let parentSection = document.getElementById(
         sectionIdPrefix.concat(sectionNumber)
      );
      parentSection.classList.add('active');
   }
}

let highlightArbitrary = (target) => {
   clear_active();
   highlightElement(target);
   highlightParentSection(target);
}

let init_listeners = () => {

   for (i = 0; i < timeline_events.length; i++) {
      timeline_events[i].addEventListener('click', (e) => {
         highlightArbitrary(e.currentTarget);
      });
   }

   for (i = 0; i < timeline_sections.length; i++) {
      timeline_sections[i].addEventListener('click', (e) => {
         highlightElement(e.currentTarget);
      });
   }
}

// init_listeners();
highlightElement(timeline_sections[0]);

// Highlight Scrolling

let c = document.querySelector("#content");
let trackedText = document.querySelectorAll('.content-tracked');
let active = []

let bind_observe = (obs) => {
   for (let i = 0; i < trackedText.length; i++) {
      obs.observe(trackedText[i]);
   }
}

let options = {
   root: c,
   rootMargin: "-30% 0px -30% 0px"
}

let callback = (entries, observer) => {
   entries.forEach((entry) => {
      // console.log(entry.target);
      if (entry.isIntersecting) {
         active.push(entry.target);
      } else {
         let index = active.indexOf(entry.target);
         active.splice(index, index+1);
      }
   });

   // console.log(active);
   let anchor = active[active.length -1].dataset.anchor;
   let timelineTarget = document.getElementById("timeline-".concat(anchor));
   // Highlight event 
   highlightArbitrary(timelineTarget);
};

let observer = new IntersectionObserver(callback, options);


bind_observe(observer);

