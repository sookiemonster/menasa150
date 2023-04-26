// Aggregate timeline variables
let timeline_sections = document.querySelectorAll('.section-header');
let timeline_events = document.querySelectorAll('.event-container');

let sectionIdPrefix = "timeline-sec-";

/**
 * Remove '.active' from all timeline elements
 */
let strip_active = () => {
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

let init_listeners = () => {
   for (i = 0; i < timeline_events.length; i++) {
      timeline_events[i].addEventListener('click', (e) => {
         // console.log(e.target);
         strip_active();
         // Highlight event 
         highlightElement(e.currentTarget);

         // Highlight event section

         let sectionNumber = e.currentTarget.closest(".event-list").dataset.sectionNo;

         highlightElement(
            document.getElementById(
               sectionIdPrefix.concat(sectionNumber)
            )
         );
      });
   }

   for (i = 0; i < timeline_sections.length; i++) {
      timeline_sections[i].addEventListener('click', (e) => {
         // console.log(e.target);
         strip_active();
         e.currentTarget.classList.add('active');
      });
   }
}

init_listeners();