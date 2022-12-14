# wd = weather.get_weather(weather.LOCATION)
# n = 10
# d1 = sensorNode(1,0)
# test_data = []
# data = []
# for i in range(n):
#     d1.gather_data(wd)
#     test_data.append([d1.temperature])

# print(f"test = {test_data}")
# print(f"valid = {d1.valid_counter}, malicious = {d1.malicious_counter}")
# # print(f"data = {data}")

# clf = OneClassSVM(gamma='auto').fit(test_data)
# d2 = sensorNode(2,0.25)
# for i in range(n):
#     d2.gather_data(wd)
#     data.append([d2.temperature])
# print(f"data = {data}")
# prediction = clf.predict(data)
# print(f"prediction = {prediction}")
# print(f"scores = {clf.score_samples(data)}")
# # for i in range(len(data)):
# #     print(f"reading = {data[i]}, classification = {prediction[i]}")
# print(Counter(prediction))