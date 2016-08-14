from crontab import CronTab

def schedule():
    cron = CronTab()
    job = cron.new(command="curl http://localhost:8000/register", comment="register")
    job.setall('* * * * *')
    job.enable()

    clean = cron.new(command="curl http://localhost:8000/clean", comment="clean")
    clean.setall('0 22 * * *')
    clean.enable()

    cron.write(user=True)
    print "Registered cron tabs"
schedule()
