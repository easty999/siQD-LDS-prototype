// proposed dry-sample holder, mm. unprinted, fit validation required.
// part = "tray", "spacer", "mask", or "assembly".
part="tray";
slide_l=75; slide_w=25; clearance=0.4;
outer_l=90; outer_w=38; height=4; floor=2;
aperture=20; spacer_height=8;
assert(slide_w+clearance<outer_w);
assert(slide_l+clearance<outer_l);
assert(aperture<slide_w);
module tray(){
 difference(){
  translate([-outer_l/2,-outer_w/2,0]) cube([outer_l,outer_w,height]);
  translate([-(slide_l+clearance)/2,-(slide_w+clearance)/2,floor])
    cube([slide_l+clearance,slide_w+clearance,height]);
  translate([-aperture/2,-aperture/2,-1]) cube([aperture,aperture,height+2]);
 }
}
module spacer(){cube([8,8,spacer_height]);}
module mask(){difference(){cube([30,30,1]);translate([5,5,-1])cube([20,20,3]);}}
if(part=="tray")tray();
if(part=="spacer")spacer();
if(part=="mask")mask();
if(part=="assembly"){
 translate([0,0,spacer_height])tray();
 for(x=[-45,37])for(y=[-19,11])translate([x,y,0])spacer();
 // transparent slide is only a dimensional envelope, not a printed part
 color([0.3,0.7,1,0.3])translate([-37.5,-12.5,spacer_height+floor])cube([75,25,1]);
}
