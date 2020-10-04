package elasticsearch;

import java.io.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
//import org.apache.hadoop.util.GenericOptionsParser;
//import org.apache.commons.*;
//import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
//import org.apache.hadoop.mapred.*;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
//import org.apache.hadoop.mapreduce.lib.output.*;

import org.elasticsearch.hadoop.mr.EsOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
//import org.apache.hadoop.*;

public class EsDriver {
	public static class EsMapper extends Mapper<Object, Text, NullWritable, Text> {
	    private Text doc = new Text();
	    @Override
	    protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
	        if (value.getLength() > 0) {
	             doc.set(value);
	             context.write(NullWritable.get(), doc);
	        }
	    }
	}
      
        public static void main(String[] args) throws Exception{

            org.apache.hadoop.conf.Configuration Conf
            = new org.apache.hadoop.conf.Configuration();

            Path inputPath = new Path(args[0]);
            Path outputDir = new Path(args[1]);
            
            Configuration conf = new Configuration();
            conf.setBoolean("mapreduce.map.speculative", false);
            conf.setBoolean("mapreduce.reduce.speculative", false);
            conf.set("es.nodes", "localhost:9200");
            //conf.set("es.net.http.auth.user", "FidelLinux");
            //conf.set("es.net.http.auth.pass", "fidel34335");
            //conf.set("es.net.ssl", "true");
            //conf.set("es.nodes.discovery","true");
            conf.set("es.resource", "index1/simpleText");
            conf.set("es.input.json", "yes");

            Job job = Job.getInstance(conf);

            job.setJarByClass(EsDriver.class);
            job.setMapperClass(EsMapper.class);

            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(EsOutputFormat.class);
            
            job.setMapOutputKeyClass(NullWritable.class);
            job.setMapOutputValueClass(Text.class);
            
            job.setInputFormatClass(TextInputFormat.class);
            job.setOutputFormatClass(EsOutputFormat.class);

            FileInputFormat.addInputPath(job, inputPath);
            FileOutputFormat.setOutputPath(job, outputDir);

            //job.addFileToClassPath(JobHelper.addJarToDistributedCache(EsOutputFormat.class, conf));
            //job.addFileToClassPath(JobHelper.addJarToDistributedCache(ProtocolSocketFactory.class, conf));

            // Delete output if exists
                            FileSystem hdfs = FileSystem.get(Conf);
                            if (hdfs.exists(outputDir))
                                    hdfs.delete(outputDir, true);
                            
                         	
            job.addFileToClassPath(new Path("~/Downloads/elasticsearch-hadoop-7.9.1/dist/*"));              	
            System.exit(job.waitForCompletion(true) ?0 :1);
                    
        }

       }
               