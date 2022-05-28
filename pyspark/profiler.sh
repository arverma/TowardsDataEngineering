spark-submit --master local[2] \
--jar sparklens-0.3.0-s_2.11.jar \
--conf spark.extraListeners=com.qubole.sparklens.QuboleJobListener \
main.py

spark-submit --master local[2] \
--conf spark.jars=jvm-profiler-1.0.0.jar \
--conf spark.executor.extraJavaOptions=-javaagent:jvm-profiler-1.0.0.jar \
main.py

spark-submit --master yarn --queue DE --deploy-mode cluster \
--conf spark.jars=jvm-profiler-1.0.0.jar \
--conf spark.executor.extraJavaOptions=-javaagent:jvm-profiler-1.0.0.jar \
main.py

spark-submit --master yarn --queue DE --deploy-mode cluster \
--files ./babar-agent-0.2.0-SNAPSHOT.jar \
--conf spark.executor.extraJavaOptions="-javaagent:./babar-agent-0.2.0-SNAPSHOT.jar=StackTraceProfiler,JVMProfiler[reservedMB=2560],ProcFSProfiler" \
main.py