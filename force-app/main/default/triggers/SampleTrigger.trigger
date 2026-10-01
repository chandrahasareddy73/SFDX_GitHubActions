trigger SampleTrigger on Account (before insert) {
Account[] Acc = Trigger.new;
SampleApex.applyDiscount(Acc);
}