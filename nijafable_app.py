from sugar.activity import activity

class nijafableActivity(activity.Activity):
    '''
    The base class for the nijafable activity.
    '''
    
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        
    def write_file(self, file_path):
        '''
        Implement this method to save your activity's state.
        '''
        raise NotImplementedError
    
    def read_file(self, file_path):
        '''
        Implement this method to resume state saved in write_file().
        '''
        raise NotImplementedError
#de ninjas que pelean www.ninjafable.com