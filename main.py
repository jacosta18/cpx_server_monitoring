import argparse
import time

def print_running_services(cpx):
    # code to query CPX for running services and print table to stdout
    services = cpx.get_running_services()
    print("Service Name\tCPU\tMemory")
    for service in services:
        print("{}\t{}\t{}".format(service.name, service.cpu, service.memory))

def print_avg_cpu_memory(cpx, service_type):
    # code to query CPX for services of type `service_type` and print average CPU/Memory
    services = cpx.get_services_by_type(service_type)
    total_cpu = 0
    total_memory = 0
    for service in services:
        total_cpu += service.cpu
        total_memory += service.memory
    avg_cpu = total_cpu / len(services)
    avg_memory = total_memory / len(services)
    print("Average CPU: {}".format(avg_cpu))
    print("Average Memory: {}".format(avg_memory))

def flag_unhealthy_services(cpx):
    # code to query CPX for services with fewer than 2 healthy instances and flag them
    services = cpx.get_running_services()
    for service in services:
        if service.healthy_instances < 2:
            print("Service {} has fewer than 2 healthy instances.".format(service.name))

def track_cpu_memory(cpx, service_name):
    # code to track CPU/Memory of all instances of `service_name` until ctrl + c is pressed
    service = cpx.get_service_by_name(service_name)
    print("Instance Name\tCPU\tMemory")
    while True:
        for instance in service.instances:
            print("{}\t{}\t{}".format(instance.name, instance.cpu, instance.memory))
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Query Cloud Provider X (CPX)")
    parser.add_argument("--running-services", action="store_true", help="Print running services")
    parser.add_argument("--avg-cpu-memory", type=str, help="Print average CPU/Memory of services of type")
    parser.add_argument("--unhealthy", action="store_true", help="Flag services with fewer than 2 healthy instances")
    parser.add_argument("--track-cpu-memory", type=str, help="Track and print CPU/Memory of all instances of a service")
    args = parser.parse_args()

    cpx = "value" # replace with code to initialize connection to CPX

    if args.running_services:
        print_running_services(cpx)
    elif args.avg_cpu_memory:
        print_avg_cpu_memory(cpx, args.avg_cpu_memory)
    elif args.unhealthy:
        flag_unhealthy_services(cpx)
    elif args.track_cpu_memory:
        track_cpu_memory()