import numpy as np
from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

# Load the MovieLens 100k data set. Only five star ratings are treated as positive.
data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))

# Instantiate and train the model. warp = Weighted Approximate-Rank Pairwise.
# Predicting by gradient descent both over user content + collaborate = hybrid.
# Runs for this training set is 30, with parallel threads to 2
model = LightFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)


def sample_recommendations(model, data, user_ids):
    # number of users and movies in training data
    n_users, n_items = data['train'].shape

    # generate recommendations for each user we input
    for user_id in user_ids:

        # movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        # movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        # rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        # print out the results
        print('user %s' % user_id)
        print('  known positives:')

        for x in known_positives[:3]:
            print('    %s' % x)

        print('  recommended:')
        for x in top_items[:3]:
            print('    %s' %x)

sample_recommendations(model, data, [3, 25, 450])

