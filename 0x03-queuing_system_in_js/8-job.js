import kue from 'kue';

const queue = kue.createQueue();
const  queueName = 'push_notification_code_3';

const createPushNotificationsJobs = (jobs, queues) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobObj) => {
    const job = queue.create(queueName, jobObj);

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    
    job.on('failed', (err)  => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
  });

};

module.exports = createPushNotificationsJobs;
