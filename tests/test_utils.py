
from fundamentus import utils

import pandas as pd


def test_dt_iso8601_10_10():
    assert utils.dt_iso8601('10/10/2020') == '2020-10-10'

def test_dt_iso8601_10_01():
    assert utils.dt_iso8601('01/10/2020') == '2020-10-01'

def test_dt_iso8601_01_10():
    assert utils.dt_iso8601('10/01/2020') == '2020-01-10'



def test_from_pt_br_01():
    _before =  pd.DataFrame( { 'data': [ '?tst','tst()','tst$./','tst tst','tst__' ]} )
    _after  =  pd.DataFrame( { 'data': [ 'tst' ,'tst'  ,'tst'   ,'tst_tst','tst_'  ]} )
    _test   = utils.from_pt_br(_before['data'])

    pd.testing.assert_frame_equal(_test.to_frame(), _after)


def test_from_pt_br_02():
    _before =  pd.DataFrame( { 'data': [ 'mês','Únicoúnico','imóvel','média adíção','tst b' ]} )
    _after  =  pd.DataFrame( { 'data': [ 'mes','Unicounico','imovel','media_adicao','tst_b' ]} )
    _test   = utils.from_pt_br(_before['data'])

    pd.testing.assert_frame_equal(_test.to_frame(), _after)



def test_fmt_dec():
    more_data = { 'col1': [ 11,21],
                  'col2': [ 12,22],
                  'col3': [ 13,23]}
    b = { 'data': [ '45,56%','1.045,56%' ]}
    b.update(more_data)
    a = { 'data': [ '45.56%','1045.56%'  ]}
    a.update(more_data)

    _before = pd.DataFrame(b)
    _after  = pd.DataFrame(a)

    _before['data'] = utils.fmt_dec(_before['data'])
    pd.testing.assert_frame_equal(_before, _after)



def test_perc_to_float():
    more_data = { 'col1': [ 11,21],
                  'col2': [ 12,22],
                  'col3': [ 13,23]}
    b = { 'data': [ '45,56%','1.045,56%' ]}
    b.update(more_data)
    a = { 'data': [   0.4556, 10.4556    ]}
    a.update(more_data)

    _before = pd.DataFrame(b)
    _after  = pd.DataFrame(a)


    _before['data'] = utils.perc_to_float(_before['data'])
    pd.testing.assert_frame_equal(_before, _after)

