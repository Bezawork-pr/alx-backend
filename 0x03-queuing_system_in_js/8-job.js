function createPushNotificationsJobs(jobs, queue) {
  if(!Array.isArray(jobs)) throw new Error('Jobs is not an array');
  jobs.forEach((job) => {
    const createJob = queue.create('push_notification_code_3', job);
    createJob
      .on('complete', () => console.log(`Notification job ${createJob.id} completed`))
      .on('failure', (error) => console.log(`Notification job ${createJob.id} failed: ${error}`))
      .on('progress', (progress) => console.log(`Notification job ${createJob.id} ${progress}% complete`));
    createJob.save((err) => {
      if(!err) console.log(`Notification job created: ${createJob.id}`);
    })

  })
}
module.exports = createPushNotificationsJobs;
