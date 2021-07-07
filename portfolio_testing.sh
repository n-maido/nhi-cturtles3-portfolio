#!/bin/bash

# 3.03 ex3
# Objective: Test every endpoint of portfolio and print the success/error msgs

function test_endpts(){
	test_data="username=$1&password=$2"
	portfolio_url="https://nhi-hawksbills.duckdns.org" #change back to https when we containerize nginx

	# test health
	echo "Testing /health..."
    status_code=$(curl -s -o response.txt -w "%{http_code}" "$portfolio_url/health")
    handle_response $status_code

    # test register-GET
    printf "Testing /register...\n"
    status_code=$(curl -s -o response.txt -w "%{http_code}" "$portfolio_url/register")
    handle_response $status_code

    # test register-POST
    status_code=$(curl -s -o response.txt -w "%{http_code}" -X POST -d "$test_data" "$portfolio_url/register")
    handle_response $status_code


    # test login-GET
    printf "\nTesting /login...\n"
    status_code=$(curl -s -o response.txt -w "%{http_code}" "$portfolio_url/register")
    handle_response $status_code

    # test login-POST
    status_code=$(curl -s -o response.txt -w "%{http_code}" -X POST -d "$test_data" "$portfolio_url/login")
    handle_response $status_code
}

function handle_response(){
    status_code=$1

    if [[ $status_code -eq 200 || -z $status_code ]]; then
        printf "SUCCESS\n"
    else
        printf "ERROR: Request returned status code $status_code\n"
    fi
    
}
