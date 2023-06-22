const kue = require('kue');
const createPushNotificationsJobs = require('./8-job.js');
const expect = require('chai').expect;
const queue = kue.createQueue();
const jobs = [ 
  { 
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  }
]
before(function() {
  queue.testMode.enter();
});
afterEach(function() {
  queue.testMode.clear();
});
after(function() {
  queue.testMode.exit();
});
it('None array passed', () => {
  expect(() => {
     createPushNotificationsJobs(5, queue);
  }).to.throw('Jobs is not an array');
});
