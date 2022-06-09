from material import User, TrafficUsageDao, TrafficUsage
from service import TrafficUsageService

if __name__ == '__main__':
    class SampleTrafficUsageDao(TrafficUsageDao):
        def load_all(self):
            a100 = User('a100', 'Ali', 20)
            a101 = User('a101', 'Hasan', 19)
            a102 = User('a102', 'Mehri', 35)
            a103 = User('a103', 'Babak', 54)
            a104 = User('a104', 'Sara', 22)
            a105 = User('a105', 'Reza', 33)
            a106 = User('a106', 'Javad', 44)
            a107 = User('a107', 'Mohammad', 55)
            a108 = User('a108', 'Ali', 18)
            a109 = User('a109', 'Elahe', 29)

            return [
                TrafficUsage(a100, True, False, 100, '97/04/01'), TrafficUsage(a100, False, True, 150, '97/04/01'),
                TrafficUsage(a100, False, False, 100, '97/04/03'), TrafficUsage(a100, True, True, 100, '97/04/04'),
                TrafficUsage(a100, True, False, 100, '97/06/01'), TrafficUsage(a100, False, True, 150, '97/06/01'),
                
                TrafficUsage(a101, True, False, 90, '97/04/01'), TrafficUsage(a101, False, True, 100, '97/04/01'),
                TrafficUsage(a101, True, False, 90, '97/05/01'), TrafficUsage(a101, False, True, 100, '97/05/01'),
                
                TrafficUsage(a102, True, False, 90, '97/04/01'), TrafficUsage(a102, False, True, 100, '97/04/01'),
                TrafficUsage(a102, True, False, 90, '97/05/01'), TrafficUsage(a102, False, True, 100, '97/05/01'),
                
                TrafficUsage(a103, True, False, 100, '97/04/01'), TrafficUsage(a103, False, True, 100, '97/04/01'),
                TrafficUsage(a103, True, False, 100, '97/05/01'), TrafficUsage(a103, False, True, 100, '97/05/01'),
                
                TrafficUsage(a104, True, False, 100, '97/04/01'), TrafficUsage(a104, False, True, 100, '97/04/01'),
                TrafficUsage(a104, True, False, 100, '97/05/01'), TrafficUsage(a104, False, True, 100, '97/05/01'),
                
                TrafficUsage(a105, True, False, 100, '97/04/01'), TrafficUsage(a105, False, True, 100, '97/04/01'),
                TrafficUsage(a105, True, False, 100, '97/05/01'), TrafficUsage(a105, False, True, 100, '97/05/01'),
                TrafficUsage(a105, True, False, 100, '97/06/01'), TrafficUsage(a105, False, True, 100, '97/06/01'),
                
                TrafficUsage(a106, True, False, 100, '97/04/01'), TrafficUsage(a106, False, True, 100, '97/04/01'),
                TrafficUsage(a106, True, False, 100, '97/05/01'), TrafficUsage(a106, False, True, 100, '97/05/01'),
                
                TrafficUsage(a107, True, False, 100, '97/04/01'), TrafficUsage(a107, False, True, 100, '97/04/01'),
                TrafficUsage(a107, True, False, 100, '97/05/01'), TrafficUsage(a107, False, True, 100, '97/05/01'),
                
                TrafficUsage(a108, True, False, 100, '97/04/01'), TrafficUsage(a108, False, True, 100, '97/04/01'),
                TrafficUsage(a108, True, False, 100, '97/05/01'), TrafficUsage(a108, False, True, 100, '97/05/01'),
                
                TrafficUsage(a109, True, False, 400, '97/04/01'), TrafficUsage(a109, False, True, 200, '97/04/01'),
                TrafficUsage(a109, True, False, 100, '97/05/01'), TrafficUsage(a109, False, True, 300, '97/05/01'),
            ]

    service = TrafficUsageService(traffic_usage_dao=SampleTrafficUsageDao())

    print('social media lovers:')
    for user in service.social_media_lovers(97, 4):
        print(user)

    print('download lovers:')
    for user in service.download_lovers(97, 4):
        print(user)
