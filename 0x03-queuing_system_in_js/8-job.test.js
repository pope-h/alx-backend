import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create a queue in test mode
    queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1', db: 3 } });
    queue.testMode.enter();
  });

  after(() => {
    // Clear the queue and exit test testMode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Hello' },
      { phoneNumber: '4153518781', message: 'Hi' },
      { phoneNumber: '4153518782', message: 'Hey' }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Get the list of jobs in the queue
    const jobsInQueue = queue.testMode.jobs;

    // Check if the correct number of jobs has been created
    expect(jobsInQueue.length).to.equal(3);
    
    // Check if each job has been created with the correct data
    expect(jobsInQueue[0].type).to.equal('push_notification_code_3');
    expect(jobsInQueue[0].data).to.eql({ phoneNumber: '4153518780', message: 'Hello' });

    expect(jobsInQueue[1].type).to.equal('push_notification_code_3');
    expect(jobsInQueue[1].data).to.eql({ phoneNumber: '4153518781', message: 'Hi' });

    expect(jobsInQueue[2].type).to.equal('push_notification_code_3');
    expect(jobsInQueue[2].data).to.eql({ phoneNumber: '4153518782', message: 'Hey' });
  });
});
