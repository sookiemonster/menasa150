let timeline_events = document.querySelectorAll('.event-container');

let strip_events = () => {
   for (i = 0; i < timeline_events.length; i++) {
      timeline_events[i].classList.remove('active');
   }
}

for (i = 0; i < timeline_events.length; i++) {
   timeline_events[i].addEventListener('click', (e) => {
      console.log(e.target);
      strip_events();
      e.currentTarget.classList.add('active');
   });
}