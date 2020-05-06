var source = new EventSource('http://live-test-scores.herokuapp.com/scores');
source.onmessage = function eventHandler(event) {
  alert(event.data);
};
source.addEventListener('any', eventHandler, false);
console.log('in js file')