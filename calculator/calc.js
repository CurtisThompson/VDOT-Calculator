var dict_time_to_vdot = {
	"1500" : {"Intercept" : 329.27860150668084,"Coef1" : -2.2878652954334515,"Coef2" : 0.007368647248557065,"Coef3" : -1.1347303996810042e-05,"Coef4" : 6.745712681152649e-09,},
	"Mile" : {"Intercept" : 324.76483573891585,"Coef1" : -2.0716951739709533,"Coef2" : 0.006141200560786788,"Coef3" : -8.718241114900932e-06,"Coef4" : 4.783091986718113e-09,},
	"3k" : {"Intercept" : 313.7203572479981,"Coef1" : -0.9881740609613102,"Coef2" : 0.0014579785952588678,"Coef3" : -1.0370717538637814e-06,"Coef4" : 2.861903218749628e-10,},
	"2-mile" : {"Intercept" : 316.1330922667594,"Coef1" : -0.9279017982428408,"Coef2" : 0.0012757152590783599,"Coef3" : -8.458729346485425e-07,"Coef4" : 2.1764323850093084e-10,},
	"5k" : {"Intercept" : 320.21840994212795,"Coef1" : -0.5853384526205057,"Coef2" : 0.0004993869890362002,"Coef3" : -2.0566501072342214e-07,"Coef4" : 3.29250289142144e-11,},
	"8k" : {"Intercept" : 327.6911338755366,"Coef1" : -0.3680495210128639,"Coef2" : 0.00019187022410882505,"Coef3" : -4.812223308422301e-08,"Coef4" : 4.683591242702484e-12,},
	"5-mile" : {"Intercept" : 328.49917001063824,"Coef1" : -0.3673895725160274,"Coef2" : 0.00019066831304996105,"Coef3" : -4.759668180544504e-08,"Coef4" : 4.609870346778192e-12,},
	"10k" : {"Intercept" : 330.2139691291625,"Coef1" : -0.29512088073493226,"Coef2" : 0.00012221786339786266,"Coef3" : -2.4325848802344985e-08,"Coef4" : 1.877863099394861e-12,},
	"15k" : {"Intercept" : 326.95870507570623,"Coef1" : -0.1899108318084571,"Coef2" : 5.1247425374576816e-05,"Coef3" : -6.648611772557914e-09,"Coef4" : 3.3438648307541554e-13,},
	"10-mile" : {"Intercept" : 326.2893207965112,"Coef1" : -0.17562364203528766,"Coef2" : 4.395062988286604e-05,"Coef3" : -5.289882638239394e-09,"Coef4" : 2.4684527561097754e-13,},
	"20k" : {"Intercept" : 323.54693717028204,"Coef1" : -0.1377154099842604,"Coef2" : 2.7321429785576135e-05,"Coef3" : -2.6102540489023597e-09,"Coef4" : 9.672793368684617e-14,},
	"1/2 Marathon" : {"Intercept" : 322.4469083515478,"Coef1" : -0.12946198359807962,"Coef2" : 2.424316208779521e-05,"Coef3" : -2.1871374507139768e-09,"Coef4" : 7.655120908369763e-14,},
	"25k" : {"Intercept" : 322.2697198388745,"Coef1" : -0.10755482241534677,"Coef2" : 1.675650481882731e-05,"Coef3" : -1.2597341869766555e-09,"Coef4" : 3.6783022374503593e-14,},
	"30k" : {"Intercept" : 321.82166748993717,"Coef1" : -0.08825842204715381,"Coef2" : 1.1309783024971546e-05,"Coef3" : -7.004631158326267e-10,"Coef4" : 1.686803942238611e-14,},
	"Marathon" : {"Intercept" : 321.12012648726966,"Coef1" : -0.06136506076550384,"Coef2" : 5.4868477889635125e-06,"Coef3" : -2.3765834419263595e-10,"Coef4" : 4.008787557821265e-15,},
};

var dict_vdot_to_pace = {
	"EL" : {"Intercept" : 1111.6245911844676,"Coef1" : -35.01259939298468,"Coef2" : 0.5916019671951158,"Coef3" : -0.005023023269912746,"Coef4" : 1.6900232069239074e-05,},
	"M" : {"Intercept" : 1009.9104968142364,"Coef1" : -33.00843297164567,"Coef2" : 0.5696263495261077,"Coef3" : -0.0049305273474878385,"Coef4" : 1.6891114138828378e-05,},
	"T" : {"Intercept" : 929.2324123006365,"Coef1" : -30.098368229861034,"Coef2" : 0.5149537640256838,"Coef3" : -0.0043927868247877816,"Coef4" : 1.4802713471206985e-05,},
	"I" : {"Intercept" : 996.2679395844403,"Coef1" : -38.465301917691995,"Coef2" : 0.7671644369446106,"Coef3" : -0.007451978113829883,"Coef4" : 2.7952897172833783e-05,},
	"R" : {"Intercept" : 1005.9074909330948,"Coef1" : -40.7128865503877,"Coef2" : 0.8288693283243007,"Coef3" : -0.008167427307772316,"Coef4" : 3.095572620737119e-05,},
};

var dict_vdot_to_time = {
	"1500" : {"Intercept" : 1362.7441522914985,"Coef1" : -48.264652725368144,"Coef2" : 0.8653754288689459,"Coef3" : -0.007641745955043459,"Coef4" : 2.652375951783803e-05,},
	"Mile" : {"Intercept" : 1480.7156225327951,"Coef1" : -52.774070825912744,"Coef2" : 0.952135413380356,"Coef3" : -0.008457318854870088,"Coef4" : 2.9503073592840327e-05,},
	"3k" : {"Intercept" : 2755.3660645183368,"Coef1" : -93.66540590640359,"Coef2" : 1.6362379482993907,"Coef3" : -0.014189438014280326,"Coef4" : 4.853447463748495e-05,},
	"2-mile" : {"Intercept" : 2969.8161536801576,"Coef1" : -101.25207919983316,"Coef2" : 1.7782980476958696,"Coef3" : -0.015517270675989056,"Coef4" : 5.341102006006793e-05,},
	"5k" : {"Intercept" : 4682.663640421648,"Coef1" : -159.17486639507186,"Coef2" : 2.8036060176782325,"Coef3" : -0.02452391487791017,"Coef4" : 8.450086440081607e-05,},
	"8k" : {"Intercept" : 7777.345177265712,"Coef1" : -266.2554824519657,"Coef2" : 4.703039667210354,"Coef3" : -0.04112842423027405,"Coef4" : 0.0001414956806842227,},
	"5-mile" : {"Intercept" : 7824.772710582121,"Coef1" : -267.9674863968673,"Coef2" : 4.736374663550012,"Coef3" : -0.04145820835037413,"Coef4" : 0.00014279261116634243,},
	"10k" : {"Intercept" : 9846.37792147859,"Coef1" : -338.1957842938728,"Coef2" : 5.986958440642983,"Coef3" : -0.052429677555169016,"Coef4" : 0.00018056615360695358,},
	"15k" : {"Intercept" : 15096.287182028584,"Coef1" : -514.9512113931958,"Coef2" : 9.05259179731292,"Coef3" : -0.07887609495378023,"Coef4" : 0.0002707373983561468,},
	"10-mile" : {"Intercept" : 16224.07319712835,"Coef1" : -551.585284825309,"Coef2" : 9.675538370702874,"Coef3" : -0.08420090107129997,"Coef4" : 0.00028883696945847254,},
	"20k" : {"Intercept" : 20239.53297924062,"Coef1" : -681.4038540918663,"Coef2" : 11.871279031913598,"Coef3" : -0.1028613191746019,"Coef4" : 0.0003518667705684209,},
	"1/2 Marathon" : {"Intercept" : 21385.425812880967,"Coef1" : -719.0864275281987,"Coef2" : 12.517605937384017,"Coef3" : -0.10840877853966974,"Coef4" : 0.00037071373011521297,},
	"25k" : {"Intercept" : 25271.70347200604,"Coef1" : -842.0248502015579,"Coef2" : 14.605722851389013,"Coef3" : -0.12634073772655602,"Coef4" : 0.0004318964527243452,},
	"30k" : {"Intercept" : 30254.210186874752,"Coef1" : -999.8365169143964,"Coef2" : 17.289771897148047,"Coef3" : -0.1494157586913597,"Coef4" : 0.0005106780353543172,},
	"Marathon" : {"Intercept" : 42412.877897840335,"Coef1" : -1385.2115986060828,"Coef2" : 23.84922407334187,"Coef3" : -0.20585494848299984,"Coef4" : 0.000703545277715989,},
};

function secs_to_time(seconds) {
	return new Date(seconds * 1000).toISOString().substr(11, 8);
}

function secs_to_pace(seconds) {
	return new Date(seconds * 1000).toISOString().substr(14, 5);
}

function input_and_coefs(i, coef_dict) {
	m = coef_dict['Intercept'];
	c1 = coef_dict['Coef1'];
	c2 = coef_dict['Coef2'];
	c3 = coef_dict['Coef3'];
	c4 = coef_dict['Coef4'];
	
	return (m + (c1*i) + (c2*i*i) + (c3*i*i*i) + (c4*i*i*i*i));
}

function make_calcs() {
	// Time To Secs
	secs = (document.getElementById("input-hour").value * 3600) + (document.getElementById("input-minute").value * 60) + (document.getElementById("input-second").value * 1);
	
	// Get distance
	distance = document.getElementById("select-distance").value;
	
	// VDOT
	vdot = input_and_coefs(secs, dict_time_to_vdot[distance]);
	document.getElementById("output-vdot").innerHTML = Math.round(vdot * 100) / 100;
	
	// Paces
	pace_e = input_and_coefs(vdot, dict_vdot_to_pace['EL']);
	pace_m = input_and_coefs(vdot, dict_vdot_to_pace['M']);
	pace_t = input_and_coefs(vdot, dict_vdot_to_pace['T']);
	pace_i = input_and_coefs(vdot, dict_vdot_to_pace['I']);
	pace_r = input_and_coefs(vdot, dict_vdot_to_pace['R']);
	document.getElementById("output-e").innerHTML = secs_to_pace(pace_e);
	document.getElementById("output-m").innerHTML = secs_to_pace(pace_m);
	document.getElementById("output-t").innerHTML = secs_to_pace(pace_t);
	document.getElementById("output-i").innerHTML = secs_to_pace(pace_i);
	document.getElementById("output-r").innerHTML = secs_to_pace(pace_r);
	
	// Times
	time_5k = input_and_coefs(vdot, dict_vdot_to_time['5k']);
	document.getElementById("output-5k").innerHTML = secs_to_time(time_5k);
	time_10k = input_and_coefs(vdot, dict_vdot_to_time['10k']);
	document.getElementById("output-10k").innerHTML = secs_to_time(time_10k);
	time_hm = input_and_coefs(vdot, dict_vdot_to_time['1/2 Marathon']);
	document.getElementById("output-half-mara").innerHTML = secs_to_time(time_hm);
	time_m = input_and_coefs(vdot, dict_vdot_to_time['Marathon']);
	document.getElementById("output-mara").innerHTML = secs_to_time(time_m);
}