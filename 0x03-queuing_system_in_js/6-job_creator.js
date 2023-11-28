import { createQueue } from 'kue';

const jobs = [
  {phoneNumber: '1234556',
    message: 'This is the code 1234 to verify your account'
  }

];

const queue = createQueue();

jobs.forEach((myJob) => {
  let job = queue.create('push_notification_code_2', myJob).save((error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
  });

  job.on('complete', function() {
    console.log(`Notification job ${job.id} completed`);
  }).on('failed', function(error) {
    console.log(`Notification job ${job.id} failed: ${error}`);
  }).on('progress', function(progress, data) {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
