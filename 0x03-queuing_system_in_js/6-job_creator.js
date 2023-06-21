const kue = require('kue');
const queue = kue.createQueue();
const jobData = {
  phoneNumber: "908743210",
  message: "Job",
}
const job = queue.create("push_notification_code", jobData).save( function(err) { 
  if (!err) console.log(job.id);
})
job.on('complete', () => console.log('Notification job completed'));
job.on('failure', () => console.log('Notification job failed'));
