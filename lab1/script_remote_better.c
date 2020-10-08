#include<stdio.h>
#include<stdlib.h>
#include <curl/curl.h>
#include <math.h>
#include <unistd.h>

// compile
// gcc script.c -o script -lcurl -lm; ./script 5

int main(int argc, char *argv[]) {
    // determine number of iterations
    int num_of_iterations = 30;
    if (argc == 2) {
        num_of_iterations = atoi(argv[1]);
    }

    double times[num_of_iterations];

    CURL *curl;
    CURLcode res;
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if(curl){
        curl_easy_setopt(curl, CURLOPT_URL, "http://34.125.29.204/cgi-bin/test.py");
        // curl_easy_setopt(curl, CURLOPT_URL, "http://localhost/cgi-bin/test.py");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "input=555");
        curl_easy_setopt(curl, CURLOPT_NOBODY, 1);

        // perform measurements
        for(int i = 0; i < num_of_iterations; i++){
            res = curl_easy_perform(curl); 
            if(res != CURLE_OK){
                fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            }
            if(CURLE_OK == res) {
                res = curl_easy_getinfo(curl, CURLINFO_TOTAL_TIME, &times[i]);
                if(CURLE_OK == res) {
                    printf("Iteration %d. Time: %.3f s\n", i, times[i]);
                }
            }
            sleep(1);
        }
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();

    // calculate confindence interval
    double mean = 0;
    double variance = 0;
    double standard_deviation = 0;
    double margin_of_error = 0;
    double z_value_95 = 1.960;
    double z_value_99 = 2.576;
    for(int i = 0; i < num_of_iterations; i++){
        mean += times[i];
    }
    mean = mean / num_of_iterations;
    for(int i = 0; i < num_of_iterations; i++){
        variance += pow(fabs(mean - times[i]), 2);
    }
    variance = variance / num_of_iterations;
    standard_deviation = sqrt(variance);
    margin_of_error = z_value_95 * standard_deviation/sqrt(num_of_iterations);

    printf("number of iterations: %d\n", num_of_iterations);
    printf("mean: %f s, variance: %f, standard deviation: %f\n", mean, variance, standard_deviation);
    printf("margin of error: %f s\n", margin_of_error);
    printf("with 95%% the confidence interval is between %f s and %f s\n", mean - margin_of_error, mean + margin_of_error);

    return 0;
}