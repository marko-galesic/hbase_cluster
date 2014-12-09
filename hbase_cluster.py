import boto.emr

emrConnection = boto.emr.connection.EmrConnection()


log_uri = "s3://log-uri"
ec2_keyname = "key_name"
availability_zone = "us-east-1d"

# Install HBase step parameters
hbase_jar = /home/hadoop/lib/hbase.jar
hbase_jar_main = "emr.hbase.backup.Main"
hbase_arguments = ["--start-master"]


# HBaes Jar step
start_hbase = boto.emr.JarStep(name = "Start HBase", jar = hbase_jar, main_class = hbase_jar_main, action_on_failure = "TERMIANTE_CLUSTER", step_args = hbase_arguments)

hbase_cluster_steps = [boto.emr.step.InstallHiveStep, boto.emr.step.InstallPigStep]

emrConnection.run_jobflow(name = "HBase-Cluster", log_uri=log_uri, ec2_keyname=ec2_keyname, availability_zone=availability_zone)