#!/usr/bin/env bash
#   Use this script to run up docker compose test

docker-compose -f docker-compose.rabbit-actix.test.yml build --build-arg http_proxy=http://jiangqizhou-001:1234.Ding@10.228.110.21:8002 --build-arg https_proxy=http://jiangqizhou-001:1234.Ding@10.228.110.21:8002