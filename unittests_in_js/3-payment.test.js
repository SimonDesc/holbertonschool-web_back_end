import * as chai from 'chai';
const expect = chai.expect;
import sinon from 'sinon';
import Utils from './utils.js'
import sendPaymentRequestToApi from './3-payment.js'

describe('sendPaymentRequestToApi', function () {
  it('making sure the function is called', function () {
    const spyUtils = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);

    expect(spyUtils.calledOnce).to.be.true;
    expect(spyUtils.calledWith('SUM', 100, 20)).to.be.true;
    spyUtils.restore();
  });
});
