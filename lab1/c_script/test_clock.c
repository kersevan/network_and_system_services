#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>
#include <math.h>
#include <unistd.h>
#include <time.h>

// compile
// gcc script_remote.c -o script_remote -lcurl -lm; ./script_remote 5

int main(int argc, char *argv[]) {
    // determine number of iterations
    int num_of_iterations = 30;
    if (argc == 2) {
        num_of_iterations = atoi(argv[1]);
    }

    double times[num_of_iterations];

    clock_t start;
    clock_t end;

    CURL *curl;
    CURLcode res;
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if(curl){
        curl_easy_setopt(curl, CURLOPT_URL, "http://34.125.29.204/cgi-bin/test.py");
        // curl_easy_setopt(curl, CURLOPT_URL, "http://localhost/cgi-bin/test.py");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "input=555");
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);

        // perform measurements
        for(int i = 0; i < num_of_iterations; i++){
            start = clock();
            res = curl_easy_perform(curl); 
            end = clock();
            times[i] = ((double)(end-start))/CLOCKS_PER_SEC;
            if(res != CURLE_OK){
                fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            } else {
                // res = curl_easy_getinfo(curl, CURLINFO_TOTAL_TIME, &times[i]);
                printf("Iteration %d. Time: %g s\n", i, times[i]);
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

    // write results to file
    time_t t;
    FILE *file = fopen("results_remote.txt", "a");
    time(&t);
    fprintf(file, "current time is : %s",ctime(&t));
    fprintf(file, "number of iterations: %d\n", num_of_iterations);
    fprintf(file, "mean: %f s, variance: %f, standard deviation: %f\n", mean, variance, standard_deviation);
    fprintf(file, "margin of error: %f s\n", margin_of_error);
    fprintf(file, "with 95%% the confidence interval is between %f s and %f s\n\n", mean - margin_of_error, mean + margin_of_error);

    fclose(file);

    return 0;
}
