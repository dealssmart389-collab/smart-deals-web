def get_blood_flow(branch):
    flow = {'tab1': 'Wisdom', 'tab2': 'Deals', 'tab3': 'Security'}
    return flow.get(branch, 'Unknown')
