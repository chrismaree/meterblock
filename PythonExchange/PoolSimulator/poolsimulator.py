import time

hour = 0;

consumerA = 0
consumerB = 0

producerA_produced = 0
producerB_produced = 0

producerA_paid = 0
producerB_paid = 0
while True:
    if hour==24: #end of day
        hour = 0
        totalPool = consumerA+consumerB
        producerA_paid = producerA_produced / totalPool
        producerB_paid = producerB_produced / totalPool



    consumerA += 10
    consumerB += 25

    producerA_produced += 15
    producerB_produced += 20

    print(hour)
    time.sleep(0.5)
    hour+=1