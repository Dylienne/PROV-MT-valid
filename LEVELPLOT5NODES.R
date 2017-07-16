library('lattice')
library('party')

distance < data$orig_destination_distance
data <- sample_test_5000

distance <- data$orig_destination_distance
locationid <- data$visitor_location_country_id
destinationid <- data$srch_destination_id

levelplot(distance ~ locationid * destinationid, data = data, cuts = 9, col.regions = rainbow(10)[10:1])

paralellplot(~data[1:4] | locationid, data = data)

rating <- data$prop_starrating
visitor_ctree <- ctree(rating ~ distance + locationid + destinationid, data = data)
plot(visitor_ctree, xlim= 40)
print(visitor_ctree)


