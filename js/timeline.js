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

let init_listeners = () => {
   for (i = 0; i < timeline_events.length; i++) {
      timeline_events[i].addEventListener('click', (e) => {
         // console.log(e.target);
         clear_active();
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
         clear_active();
         e.currentTarget.classList.add('active');
      });
   }
}

init_listeners();
highlightElement(timeline_sections[0]);

// Highlight Scrolling

// let options = {
//    rootMargin: '0px',
//    threshold: 0.2
// }
 

// let callback = (entries, observer) => {
//    entries.forEach(entry => {
//       if (entry.isIntersecting){
//          clear_active();
//          console.log(entry.target);
//          let topic = entry.target.dataset.topic;
//          let navItem = document.querySelector(`a[href="#${topic}"]`).parentElement;
//          // console.log(navItem);
//          updateCurrent(navItem);
//       }
//    });
// };

// let observer = new IntersectionObserver(callback, options);

// for (let i = 0; i < topics.length; i++) {
//    observer.observe(topics[i]);
// };
