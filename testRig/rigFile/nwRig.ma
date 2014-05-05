//Maya ASCII 2011 scene
//Name: nwRig.ma
//Last modified: Sun, Sep 09, 2012 10:48:55 PM
//Codeset: 1252
requires maya "2011";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2011";
fileInfo "version" "2011";
fileInfo "cutIdentifier" "201003190014-771504";
fileInfo "osv" "Microsoft Windows XP Home Edition Service Pack 3 (Build 2600)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 28 21 28 ;
	setAttr ".r" -type "double3" -27.938352729602379 44.999999999999972 -5.172681101354183e-014 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".fcp" 1000;
	setAttr ".coi" 44.82186966202994;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".fcp" 1000;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".fcp" 1000;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".fcp" 1000;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "nwRigRoot_GRP";
	addAttr -ci true -sn "input_root" -ln "input_root" -at "message";
createNode transform -n "modules_GRP" -p "nwRigRoot_GRP";
createNode transform -n "NWSpineJointsRoot_GRP" -p "modules_GRP";
	addAttr -ci true -sn "input_root" -ln "input_root" -at "message";
createNode transform -n "NWSpineJointsBlueprint_GRP" -p "NWSpineJointsRoot_GRP";
	setAttr ".v" no;
createNode transform -n "NWSpineJointsBlueprintJoint_GRP" -p "NWSpineJointsBlueprint_GRP";
createNode joint -n "NWSpineJointsSpineChainBlueprinter0_SJNT" -p "NWSpineJointsBlueprintJoint_GRP";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWSpineJointsSpineChainBlueprinter0_PNT" -p "NWSpineJointsSpineChainBlueprinter0_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWSpineJointsSpineChainBlueprinter0_CTLW0" 
		-dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode joint -n "NWSpineJointsSpineChainBlueprinter1_SJNT" -p "NWSpineJointsSpineChainBlueprinter0_SJNT";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWSpineJointsSpineChainBlueprinter1_PNT" -p "NWSpineJointsSpineChainBlueprinter1_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWSpineJointsSpineChainBlueprinter1_CTLW0" 
		-dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode joint -n "NWSpineJointsSpineChainBlueprinter2_SJNT" -p "NWSpineJointsSpineChainBlueprinter1_SJNT";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWSpineJointsSpineChainBlueprinter2_PNT" -p "NWSpineJointsSpineChainBlueprinter2_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWSpineJointsSpineChainBlueprinter2_CTLW0" 
		-dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode joint -n "NWSpineJointsSpineChainBlueprinter3_SJNT" -p "NWSpineJointsSpineChainBlueprinter2_SJNT";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWSpineJointsSpineChainBlueprinter3_PNT" -p "NWSpineJointsSpineChainBlueprinter3_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWSpineJointsSpineChainBlueprinter3_CTLW0" 
		-dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode joint -n "NWSpineJointsSpineChainBlueprinter4_SJNT" -p "NWSpineJointsSpineChainBlueprinter3_SJNT";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWSpineJointsSpineChainBlueprinter4_PNT" -p "NWSpineJointsSpineChainBlueprinter4_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWSpineJointsSpineChainBlueprinter4_CTLW0" 
		-dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "NWSpineJointsSpineChainBlueprinterBlueprinter_GRP" -p "NWSpineJointsBlueprint_GRP";
createNode transform -n "NWSpineJointsSpineChainBlueprinter0Sctl_GRP" -p "NWSpineJointsSpineChainBlueprinterBlueprinter_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".rp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
	setAttr ".sp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
createNode transform -n "NWSpineJointsSpineChainBlueprinter0_SCTL" -p "NWSpineJointsSpineChainBlueprinter0Sctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".r" -type "double3" -95.026614449600004 23.172918618400001 -6.4607660137199998 ;
	setAttr ".s" -type "double3" 1 1 1.93203015639 ;
createNode mesh -n "NWSpineJointsSpineChainBlueprinter0_SCTLShape" -p "NWSpineJointsSpineChainBlueprinter0_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "NWSpineJointsSpineChainBlueprinter1Sctl_GRP" -p "NWSpineJointsSpineChainBlueprinter0_SCTL";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".rp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
	setAttr ".sp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
createNode transform -n "NWSpineJointsSpineChainBlueprinter1_SCTL" -p "NWSpineJointsSpineChainBlueprinter1Sctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode mesh -n "NWSpineJointsSpineChainBlueprinter1_SCTLShape" -p "NWSpineJointsSpineChainBlueprinter1_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "NWSpineJointsSpineChainBlueprinter2Sctl_GRP" -p "NWSpineJointsSpineChainBlueprinter1_SCTL";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".rp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
	setAttr ".sp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
createNode transform -n "NWSpineJointsSpineChainBlueprinter2_SCTL" -p "NWSpineJointsSpineChainBlueprinter2Sctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode mesh -n "NWSpineJointsSpineChainBlueprinter2_SCTLShape" -p "NWSpineJointsSpineChainBlueprinter2_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "NWSpineJointsSpineChainBlueprinter3Sctl_GRP" -p "NWSpineJointsSpineChainBlueprinter2_SCTL";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".rp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
	setAttr ".sp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
createNode transform -n "NWSpineJointsSpineChainBlueprinter3_SCTL" -p "NWSpineJointsSpineChainBlueprinter3Sctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode mesh -n "NWSpineJointsSpineChainBlueprinter3_SCTLShape" -p "NWSpineJointsSpineChainBlueprinter3_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "NWSpineJointsSpineChainBlueprinter4Sctl_GRP" -p "NWSpineJointsSpineChainBlueprinter3_SCTL";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".rp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
	setAttr ".sp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
createNode transform -n "NWSpineJointsSpineChainBlueprinter4_SCTL" -p "NWSpineJointsSpineChainBlueprinter4Sctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode mesh -n "NWSpineJointsSpineChainBlueprinter4_SCTLShape" -p "NWSpineJointsSpineChainBlueprinter4_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "NWSpineJointsRig_GRP" -p "NWSpineJointsRoot_GRP";
createNode transform -n "NWSpineJointsJoint_GRP" -p "NWSpineJointsRig_GRP";
createNode joint -n "NWSpineJoints1_JNT" -p "NWSpineJointsJoint_GRP";
	setAttr ".t" -type "double3" 4.0110513322979213e-018 1.0434328926436711e-016 -1.5718768294681133e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "NWSpineJoints2_JNT" -p "NWSpineJoints1_JNT";
	setAttr ".t" -type "double3" 0.15037091802335198 1.9198724534375129 -0.15562414576474828 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "NWSpineJoints3_JNT" -p "NWSpineJoints2_JNT";
	setAttr ".t" -type "double3" 0.15037091802335198 1.9198724534375129 -0.15562414576474828 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "NWSpineJoints4_JNT" -p "NWSpineJoints3_JNT";
	setAttr ".t" -type "double3" 0.15037091802335195 1.9198724534375127 -0.15562414576474831 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "NWSpineJoints5_JNT" -p "NWSpineJoints4_JNT";
	setAttr ".t" -type "double3" 0.15037091802335201 1.9198724534375131 -0.15562414576474826 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode ikEffector -n "effector1" -p "NWSpineJoints4_JNT";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "NWSpineJointsIK_CRV" -p "NWSpineJointsJoint_GRP";
createNode nurbsCurve -n "NWSpineJointsIK_CRVShape" -p "NWSpineJointsIK_CRV";
	setAttr -k off ".v";
	setAttr -s 10 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "NWSpineJointsIK_CRVShapeOrig" -p "NWSpineJointsIK_CRV";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 1 0 no 3
		6 0 0 0 7.7281206255600008 7.7281206255600008 7.7281206255600008
		4
		2.0055256661489607e-018 1.0768279586344138e-016 -3.561495976296948e-017
		0.20049456010789629 2.5598299729436 -0.20749886385893312
		0.40098911198551085 5.1196598408064462 -0.41499771920005923
		0.60148367209340758 7.679489813750048 -0.62249658305899291
		;
createNode transform -n "NWSpineJointsSetup_GRP" -p "NWSpineJointsRig_GRP";
createNode ikHandle -n "NWSpineJoints_IKH" -p "NWSpineJointsSetup_GRP";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.60148367209340792 7.6794898137500516 -0.62249658305899325 ;
	setAttr ".roc" yes;
createNode transform -n "NWSpineJointsControl_GRP" -p "NWSpineJointsRig_GRP";
createNode transform -n "NWSpineJointsIKCluster0Ctl_GRP" -p "NWSpineJointsControl_GRP";
	setAttr ".t" -type "double3" 2.0055256661489607e-018 1.0768279586344139e-016 -1.4663726222548513e-016 ;
	setAttr ".rp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
	setAttr ".sp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
createNode transform -n "NWSpineJointsIKCluster0_CTL" -p "NWSpineJointsIKCluster0Ctl_GRP";
createNode nurbsCurve -n "NWSpineJointsIKCluster0_CTLShape" -p "NWSpineJointsIKCluster0_CTL";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "NWSpineJointsIKCluster0_GRP" -p "NWSpineJointsIKCluster0_CTL";
	setAttr ".t" -type "double3" -2.0055256661489607e-018 -1.0768279586344139e-016 
		1.4663726222548513e-016 ;
	setAttr ".rp" -type "double3" 0.25 0.25000000000000011 0.24999999999999994 ;
	setAttr ".sp" -type "double3" 0.25 0.25000000000000011 0.24999999999999994 ;
createNode transform -n "NWSpineJointsIKCluster0_CLSHandle" -p "NWSpineJointsIKCluster0_GRP";
	setAttr ".rp" -type "double3" 2.0055256661489607e-018 1.0768279586344138e-016 -3.561495976296948e-017 ;
	setAttr ".sp" -type "double3" 2.0055256661489607e-018 1.0768279586344138e-016 -3.561495976296948e-017 ;
createNode clusterHandle -n "NWSpineJointsIKCluster0_CLSHandleShape" -p "NWSpineJointsIKCluster0_CLSHandle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 2.0055256661489607e-018 1.0768279586344138e-016 -3.561495976296948e-017 ;
createNode transform -n "NWSpineJointsIKCluster1Ctl_GRP" -p "NWSpineJointsIKCluster0_CTL";
	setAttr ".t" -type "double3" 0.20049456010789629 2.5598299729436 -0.2074988638589331 ;
	setAttr ".rp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
	setAttr ".sp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
createNode transform -n "NWSpineJointsIKCluster1_CTL" -p "NWSpineJointsIKCluster1Ctl_GRP";
createNode nurbsCurve -n "NWSpineJointsIKCluster1_CTLShape" -p "NWSpineJointsIKCluster1_CTL";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "NWSpineJointsIKCluster1_GRP" -p "NWSpineJointsIKCluster1_CTL";
	setAttr ".t" -type "double3" -0.20049456010789629 -2.5598299729436 0.20749886385893324 ;
	setAttr ".rp" -type "double3" 0.45049456010789624 2.8098299729436 0.042501136141066875 ;
	setAttr ".sp" -type "double3" 0.45049456010789624 2.8098299729436 0.042501136141066875 ;
createNode transform -n "NWSpineJointsIKCluster1_CLSHandle" -p "NWSpineJointsIKCluster1_GRP";
	setAttr ".rp" -type "double3" 0.20049456010789629 2.5598299729436 -0.20749886385893312 ;
	setAttr ".sp" -type "double3" 0.20049456010789629 2.5598299729436 -0.20749886385893312 ;
createNode clusterHandle -n "NWSpineJointsIKCluster1_CLSHandleShape" -p "NWSpineJointsIKCluster1_CLSHandle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.20049456010789629 2.5598299729436 -0.20749886385893312 ;
createNode transform -n "NWSpineJointsIKCluster2Ctl_GRP" -p "NWSpineJointsIKCluster1_CTL";
	setAttr ".t" -type "double3" 0.20049455187761456 2.5598298678628462 -0.20749885534112611 ;
	setAttr ".rp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
	setAttr ".sp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
createNode transform -n "NWSpineJointsIKCluster2_CTL" -p "NWSpineJointsIKCluster2Ctl_GRP";
createNode nurbsCurve -n "NWSpineJointsIKCluster2_CTLShape" -p "NWSpineJointsIKCluster2_CTL";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "NWSpineJointsIKCluster2_GRP" -p "NWSpineJointsIKCluster2_CTL";
	setAttr ".t" -type "double3" -0.40098911198551085 -5.1196598408064462 0.41499771920005935 ;
	setAttr ".rp" -type "double3" 0.6509891119855109 5.3696598408064462 -0.16499771920005923 ;
	setAttr ".sp" -type "double3" 0.6509891119855109 5.3696598408064462 -0.16499771920005923 ;
createNode transform -n "NWSpineJointsIKCluster2_CLSHandle" -p "NWSpineJointsIKCluster2_GRP";
	setAttr ".rp" -type "double3" 0.40098911198551085 5.1196598408064462 -0.41499771920005923 ;
	setAttr ".sp" -type "double3" 0.40098911198551085 5.1196598408064462 -0.41499771920005923 ;
createNode clusterHandle -n "NWSpineJointsIKCluster2_CLSHandleShape" -p "NWSpineJointsIKCluster2_CLSHandle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.40098911198551085 5.1196598408064462 -0.41499771920005923 ;
createNode transform -n "NWSpineJointsIKCluster3Ctl_GRP" -p "NWSpineJointsIKCluster2_CTL";
	setAttr ".t" -type "double3" 0.20049456010789674 2.5598299729436018 -0.20749886385893368 ;
	setAttr ".rp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
	setAttr ".sp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
createNode transform -n "NWSpineJointsIKCluster3_CTL" -p "NWSpineJointsIKCluster3Ctl_GRP";
	addAttr -ci true -sn "output_endControl" -ln "output_endControl" -at "message";
createNode nurbsCurve -n "NWSpineJointsIKCluster3_CTLShape" -p "NWSpineJointsIKCluster3_CTL";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "NWSpineJointsIKCluster3_GRP" -p "NWSpineJointsIKCluster3_CTL";
	setAttr ".t" -type "double3" -0.60148367209340758 -7.679489813750048 0.62249658305899302 ;
	setAttr ".rp" -type "double3" 0.85148367209340758 7.9294898137500489 -0.37249658305899291 ;
	setAttr ".sp" -type "double3" 0.85148367209340758 7.9294898137500489 -0.37249658305899291 ;
createNode transform -n "NWSpineJointsIKCluster3_CLSHandle" -p "NWSpineJointsIKCluster3_GRP";
	setAttr ".rp" -type "double3" 0.60148367209340758 7.679489813750048 -0.62249658305899291 ;
	setAttr ".sp" -type "double3" 0.60148367209340758 7.679489813750048 -0.62249658305899291 ;
createNode clusterHandle -n "NWSpineJointsIKCluster3_CLSHandleShape" -p "NWSpineJointsIKCluster3_CLSHandle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.60148367209340758 7.679489813750048 -0.62249658305899291 ;
createNode transform -n "NWHingeJointsRoot_GRP" -p "modules_GRP";
	addAttr -ci true -sn "input_root" -ln "input_root" -at "message";
createNode transform -n "NWHingeJointsBlueprint_GRP" -p "NWHingeJointsRoot_GRP";
	setAttr ".v" no;
createNode transform -n "NWHingeJointsBlueprintJoint_GRP" -p "NWHingeJointsBlueprint_GRP";
createNode joint -n "NWHingeJointsBaseBlueprinter_SJNT" -p "NWHingeJointsBlueprintJoint_GRP";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWHingeJointsBaseBlueprinter_PNT" -p "NWHingeJointsBaseBlueprinter_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsBaseBlueprinter_CTLW0" -dv 
		1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode joint -n "NWHingeJointsMiddleBlueprinter_SJNT" -p "NWHingeJointsBaseBlueprinter_SJNT";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWHingeJointsMiddleBlueprinter_PNT" -p "NWHingeJointsMiddleBlueprinter_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsMiddleBlueprinter_CTLW0" -dv 
		1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode joint -n "NWHingeJointsEndBlueprinter_SJNT" -p "NWHingeJointsMiddleBlueprinter_SJNT";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWHingeJointsEndBlueprinter_PNT" -p "NWHingeJointsEndBlueprinter_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsEndBlueprinter_CTLW0" -dv 1 
		-min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "NWHingeJointsBaseBlueprinterSctl_GRP" -p "NWHingeJointsBlueprint_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".rp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
	setAttr ".sp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
createNode transform -n "NWHingeJointsBaseBlueprinter_SCTL" -p "NWHingeJointsBaseBlueprinterSctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -5.8437988151100004 5.6849047664299999 1.5801202402900001 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode mesh -n "NWHingeJointsBaseBlueprinter_SCTLShape" -p "NWHingeJointsBaseBlueprinter_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "NWHingeJointsEndBlueprinterSctl_GRP" -p "NWHingeJointsBaseBlueprinter_SCTL";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr ".t" -type "double3" 0 0 2 ;
	setAttr ".rp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
	setAttr ".sp" -type "double3" -5.9604644775390625e-008 0 -8.9406967163085938e-008 ;
createNode transform -n "NWHingeJointsEndBlueprinter_SCTL" -p "NWHingeJointsEndBlueprinterSctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -5.9407871295400003 4.2841381853199998 2.72768349055 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode mesh -n "NWHingeJointsEndBlueprinter_SCTLShape" -p "NWHingeJointsEndBlueprinter_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "NWHingeJointsaxisCtl_GRP" -p "NWHingeJointsBaseBlueprinter_SCTL";
createNode transform -n "NWHingeJointsaxisCtlCtl_GRP" -p "NWHingeJointsaxisCtl_GRP";
createNode transform -n "NWHingeJointsaxisCtlXCtl_GRP" -p "NWHingeJointsaxisCtlCtl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode transform -n "NWHingeJointsaxisCtlX_CTL" -p "NWHingeJointsaxisCtlXCtl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr -l on -k off ".v";
	setAttr -k off -cb on ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "curveShape2" -p "NWHingeJointsaxisCtlX_CTL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0 0.5 0
		1 0.5 -2.2204460492503131e-016
		1 1 -2.2204460492503131e-016
		2 0 -4.4408920985006262e-016
		1 -1 -2.2204460492503131e-016
		1 -0.5 -2.2204460492503131e-016
		0 -0.5 0
		0 0.5 0
		;
createNode transform -n "NWHingeJointsaxisCtlYCtl_GRP" -p "NWHingeJointsaxisCtlCtl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode transform -n "NWHingeJointsaxisCtlY_CTL" -p "NWHingeJointsaxisCtlYCtl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -k off -cb on ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "curveShape3" -p "NWHingeJointsaxisCtlY_CTL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0 1.1102230246251565e-016 0.5
		0 1 0.49999999999999978
		0 1.0000000000000002 0.99999999999999978
		0 2 -4.4408920985006262e-016
		0 0.99999999999999978 -1.0000000000000002
		0 0.99999999999999989 -0.50000000000000022
		0 -1.1102230246251565e-016 -0.5
		0 1.1102230246251565e-016 0.5
		;
createNode transform -n "NWHingeJointsaxisCtlZCtl_GRP" -p "NWHingeJointsaxisCtlCtl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode transform -n "NWHingeJointsaxisCtlZ_CTL" -p "NWHingeJointsaxisCtlZCtl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 0 -3.29301574529 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -k off -cb on ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "curveShape4" -p "NWHingeJointsaxisCtlZ_CTL";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0 -0.5 6.123233995736766e-017
		0 -0.49999999999999989 1
		0 -0.99999999999999989 1.0000000000000002
		0 2.4492935982947064e-016 2
		0 1.0000000000000002 0.99999999999999989
		0 0.50000000000000011 0.99999999999999989
		0 0.5 -6.123233995736766e-017
		0 -0.5 6.123233995736766e-017
		;
createNode transform -n "NWHingeJointsMiddleBlueprinterSctl_GRP" -p "NWHingeJointsaxisCtlCtl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
createNode transform -n "NWHingeJointsMiddleBlueprinter_SCTL" -p "NWHingeJointsMiddleBlueprinterSctl_GRP";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode mesh -n "NWHingeJointsMiddleBlueprinter_SCTLShape" -p "NWHingeJointsMiddleBlueprinter_SCTL";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode pointConstraint -n "NWHingeJointsBaseEndConst_PNT" -p "NWHingeJointsaxisCtl_GRP";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsEndBlueprinter_SCTLW0" -dv 
		1 -min 0 -at "double";
	addAttr -ci true -k true -sn "w1" -ln "NWHingeJointsBaseBlueprinter_SCTLW1" -dv 
		1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode aimConstraint -n "NWHingeJointsBaseEndConst_AIM" -p "NWHingeJointsaxisCtl_GRP";
	addAttr -ci true -sn "w0" -ln "NWHingeJointsBaseBlueprinter_SCTLW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "NWHingeJointsDirectionSctl_GRP" -p "NWHingeJointsBlueprint_GRP";
createNode transform -n "NWHingeJointsDirection_SCTL" -p "NWHingeJointsDirectionSctl_GRP";
createNode nurbsCurve -n "curveShape1" -p "NWHingeJointsDirection_SCTL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0 0.5 0
		0 0.5 -1
		0 1 -1
		0 0 -2
		0 -1 -1
		0 -0.5 -1
		0 -0.5 0
		0 0.5 0
		;
createNode joint -n "NWHingeJointsDirection_SJNT" -p "NWHingeJointsDirection_SCTL";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode pointConstraint -n "NWHingeJointsDirection_PNT" -p "NWHingeJointsDirection_SJNT";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsDirection_CTLW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode pointConstraint -n "NWHingeJointsArrowConst_PNT" -p "NWHingeJointsDirectionSctl_GRP";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsBaseBlueprinter_SCTLW0" -dv 
		1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode aimConstraint -n "NWHingeJointsArrowConst_AIM" -p "NWHingeJointsDirectionSctl_GRP";
	addAttr -ci true -sn "w0" -ln "NWHingeJointsEndBlueprinter_SCTLW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "NWHingeJointsRig_GRP" -p "NWHingeJointsRoot_GRP";
createNode transform -n "NWHingeJointsJoint_GRP" -p "NWHingeJointsRig_GRP";
createNode joint -n "NWHingeJoints1_JNT" -p "NWHingeJointsJoint_GRP";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "NWHingeJoints2_JNT" -p "NWHingeJoints1_JNT";
	setAttr ".t" -type "double3" -5.0209199465958445 2.1420690926600008 -0.21284105556876498 ;
	setAttr ".r" -type "double3" -8.3233114537655231e-015 -2.5809564559792478e-014 8.1449474858982148e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "NWHingeJoints3_JNT" -p "NWHingeJoints2_JNT";
	setAttr ".t" -type "double3" -0.91986718294415581 2.142069092659999 4.9405245461187643 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode ikEffector -n "effector2" -p "NWHingeJoints2_JNT";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode parentConstraint -n "NWHingeJointsPole_PCT" -p "NWHingeJoints1_JNT";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsBase_CTLW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" -5.8437988151100004 5.6849047664299999 1.5801202402899999 ;
	setAttr -k on ".w0";
createNode transform -n "NWHingeJointsSetup_GRP" -p "NWHingeJointsRig_GRP";
createNode ikHandle -n "NWHingeJoints_IKH" -p "NWHingeJointsSetup_GRP";
	setAttr ".v" no;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "NWHingeJointsPole_PVC" -p "NWHingeJoints_IKH";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsPole_LOCW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" -6.8889884956989391 2.1420690926600017 -2.5602481135482424 ;
	setAttr -k on ".w0" 0.1;
createNode parentConstraint -n "NWHingeJointsIK_PCT" -p "NWHingeJoints_IKH";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsIK_CTLW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" -11.784585944650001 9.9690429517499997 6.3078037308399999 ;
	setAttr -k on ".w0";
createNode transform -n "NWHingeJointsPole_GRP" -p "NWHingeJointsSetup_GRP";
	setAttr ".rp" -type "double3" -12.732787310808938 7.8269738590900015 -0.98012787325824258 ;
	setAttr ".sp" -type "double3" -12.732787310808938 7.8269738590900015 -0.98012787325824258 ;
createNode transform -n "NWHingeJointsPole_LOC" -p "NWHingeJointsPole_GRP";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -12.732787310808938 7.8269738590900015 -0.98012787325824258 ;
createNode locator -n "NWHingeJointsPole_LOCShape" -p "NWHingeJointsPole_LOC";
	setAttr -k off ".v";
createNode parentConstraint -n "NWHingeJointsPole_PCT" -p "NWHingeJointsPole_GRP";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsPole_CTLW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 0 4.4408920985006262e-016 ;
	setAttr -k on ".w0";
createNode transform -n "NWHingeJointsControl_GRP" -p "NWHingeJointsRig_GRP";
createNode transform -n "NWHingeJointsBaseCtl_GRP" -p "NWHingeJointsControl_GRP";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
	setAttr ".t" -type "double3" -5.8437988151100004 5.6849047664299999 1.5801202402899999 ;
	setAttr ".rp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
	setAttr ".sp" -type "double3" 0 -6.1629758220391547e-033 1.1102230246251565e-016 ;
createNode transform -n "NWHingeJointsBase_CTL" -p "NWHingeJointsBaseCtl_GRP";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
createNode nurbsCurve -n "NWHingeJointsBase_CTLShape" -p "NWHingeJointsBase_CTL";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "NWHingeJointsIKCtl_GRP" -p "NWHingeJointsControl_GRP";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
createNode transform -n "NWHingeJointsIK_CTL" -p "NWHingeJointsIKCtl_GRP";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
createNode locator -n "NWHingeJointsIK_CTLShape" -p "NWHingeJointsIK_CTL";
	setAttr -k off ".v";
createNode parentConstraint -n "NWHingeJointsIK_PCT" -p "NWHingeJointsIKCtl_GRP";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsBase_CTLW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -5.9407871295399994 4.2841381853199998 4.7276834905500005 ;
	setAttr ".tg[0].tor" -type "double3" 0 3.1805546814635168e-015 0 ;
	setAttr ".rst" -type "double3" -11.784585944650001 9.9690429517499997 6.3078037308399999 ;
	setAttr -k on ".w0";
createNode transform -n "NWHingeJointsPoleCtl_GRP" -p "NWHingeJointsControl_GRP";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
createNode transform -n "NWHingeJointsPole_CTL" -p "NWHingeJointsPoleCtl_GRP";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
createNode locator -n "NWHingeJointsPole_CTLShape" -p "NWHingeJointsPole_CTL";
	setAttr -k off ".v";
createNode parentConstraint -n "NWHingeJointsIK_PCT" -p "NWHingeJointsPoleCtl_GRP";
	addAttr -ci true -k true -sn "w0" -ln "NWHingeJointsBase_CTLW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -6.8889884956989365 2.1420690926600017 -2.560248113548242 ;
	setAttr ".tg[0].tor" -type "double3" 0 3.1805546814635168e-015 0 ;
	setAttr ".rst" -type "double3" -12.732787310808938 7.8269738590900015 -0.98012787325824213 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "NWHingeJointsRoot_GRP_parentConstraint1" -p "NWHingeJointsRoot_GRP";
	addAttr -ci true -k true -sn "w0" -ln "NWSpineJointsIKCluster3_CTLW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0.60148367209340758 7.679489813750048 -0.62249658305899302 ;
	setAttr -k on ".w0";
createNode transform -n "geometry_GRP" -p "nwRigRoot_GRP";
createNode transform -n "global_GRP" -p "nwRigRoot_GRP";
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode container -n "nwRig_CNT";
	addAttr -ci true -sn "te" -ln "type" -dt "string";
	addAttr -ci true -sn "input_root" -ln "input_root" -at "message";
	addAttr -ci true -sn "ia" -ln "input_root_data" -dt "stringArray";
	addAttr -ci true -sn "re" -ln "regAttribute" -dt "stringArray";
	addAttr -ci true -sn "st" -ln "blueprint" -at "short";
	addAttr -ci true -sn "bu" -ln "rig" -at "short";
	setAttr ".isc" yes;
	setAttr ".ctor" -type "string" "Noel Wilson";
	setAttr ".cdat" -type "string" "2012/09/09 19:57:03";
	setAttr ".te" -type "string" "NWRoot";
	setAttr ".ia" -type "stringArray" 4 "type" "trans" "attr" ""  ;
	setAttr ".re" -type "stringArray" 1 "input_root"  ;
	setAttr ".st" 1;
	setAttr ".bu" 1;
createNode hyperLayout -n "hyperLayout1";
	setAttr ".ihi" 0;
	setAttr -s 6 ".hyp";
createNode container -n "NWSpineJoints_CNT";
	addAttr -ci true -sn "te" -ln "type" -dt "string";
	addAttr -ci true -sn "input_root" -ln "input_root" -at "message";
	addAttr -ci true -sn "ia" -ln "input_root_data" -dt "stringArray";
	addAttr -ci true -sn "re" -ln "regAttribute" -dt "stringArray";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	addAttr -ci true -sn "regBlueprintShape" -ln "regBlueprintShape" -at "message";
	addAttr -ci true -sn "sj" -ln "blueprinterJoints" -dt "stringArray";
	addAttr -ci true -sn "sc" -ln "blueprinterControls" -dt "stringArray";
	addAttr -ci true -sn "st" -ln "blueprint" -at "short";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
	addAttr -ci true -sn "regRigShape" -ln "regRigShape" -at "message";
	addAttr -ci true -sn "output_endControl" -ln "output_endControl" -at "message";
	addAttr -ci true -sn "oa" -ln "output_endControl_data" -dt "stringArray";
	addAttr -ci true -sn "bu" -ln "rig" -at "short";
	setAttr ".isc" yes;
	setAttr ".ctor" -type "string" "Noel Wilson";
	setAttr ".cdat" -type "string" "2012/09/09 19:57:03";
	setAttr ".te" -type "string" "NWSpineJoints";
	setAttr ".ia" -type "stringArray" 4 "type" "trans" "attr" ""  ;
	setAttr ".re" -type "stringArray" 6 "input_root" "regBlueprintTransform" "regBlueprintShape" "regRigTransform" "regRigShape" "output_endControl"  ;
	setAttr ".sj" -type "stringArray" 5 "NWSpineJointsSpineChainBlueprinter0_SJNT" "NWSpineJointsSpineChainBlueprinter1_SJNT" "NWSpineJointsSpineChainBlueprinter2_SJNT" "NWSpineJointsSpineChainBlueprinter3_SJNT" "NWSpineJointsSpineChainBlueprinter4_SJNT"  ;
	setAttr ".sc" -type "stringArray" 5 "[u'NWSpineJointsSpineChainBlueprinter0_SCTL', u'NWSpineJointsSpineChainBlueprinter0Sctl_GRP']" "[u'NWSpineJointsSpineChainBlueprinter1_SCTL', u'NWSpineJointsSpineChainBlueprinter1Sctl_GRP']" "[u'NWSpineJointsSpineChainBlueprinter2_SCTL', u'NWSpineJointsSpineChainBlueprinter2Sctl_GRP']" "[u'NWSpineJointsSpineChainBlueprinter3_SCTL', u'NWSpineJointsSpineChainBlueprinter3Sctl_GRP']" "[u'NWSpineJointsSpineChainBlueprinter4_SCTL', u'NWSpineJointsSpineChainBlueprinter4Sctl_GRP']"  ;
	setAttr ".st" 1;
	setAttr ".oa" -type "stringArray" 4 "type" "trans" "attr" ""  ;
	setAttr ".bu" 1;
createNode hyperLayout -n "hyperLayout2";
	setAttr ".ihi" 0;
	setAttr -s 97 ".hyp";
createNode polySphere -n "polySphere1";
	setAttr ".r" 0.5;
	setAttr ".sa" 1;
	setAttr ".sh" 1;
createNode polySphere -n "polySphere2";
	setAttr ".r" 0.5;
	setAttr ".sa" 1;
	setAttr ".sh" 1;
createNode polySphere -n "polySphere3";
	setAttr ".r" 0.5;
	setAttr ".sa" 1;
	setAttr ".sh" 1;
createNode polySphere -n "polySphere4";
	setAttr ".r" 0.5;
	setAttr ".sa" 1;
	setAttr ".sh" 1;
createNode polySphere -n "polySphere5";
	setAttr ".r" 0.5;
	setAttr ".sa" 1;
	setAttr ".sh" 1;
createNode container -n "NWHingeJoints_CNT";
	addAttr -ci true -sn "te" -ln "type" -dt "string";
	addAttr -ci true -sn "input_root" -ln "input_root" -at "message";
	addAttr -ci true -sn "ia" -ln "input_root_data" -dt "stringArray";
	addAttr -ci true -sn "re" -ln "regAttribute" -dt "stringArray";
	addAttr -ci true -sn "regBlueprintTransform" -ln "regBlueprintTransform" -at "message";
	addAttr -ci true -sn "regBlueprintShape" -ln "regBlueprintShape" -at "message";
	addAttr -ci true -sn "sj" -ln "blueprinterJoints" -dt "stringArray";
	addAttr -ci true -sn "sc" -ln "blueprinterControls" -dt "stringArray";
	addAttr -ci true -sn "st" -ln "blueprint" -at "short";
	addAttr -ci true -sn "regRigTransform" -ln "regRigTransform" -at "message";
	addAttr -ci true -sn "regRigShape" -ln "regRigShape" -at "message";
	addAttr -ci true -sn "bu" -ln "rig" -at "short";
	addAttr -ci true -sn "connection_endControl_root" -ln "connection_endControl_root" 
		-at "message";
	addAttr -ci true -sn "ca" -ln "connection_endControl_root_data" -dt "stringArray";
	setAttr ".isc" yes;
	setAttr ".ctor" -type "string" "Noel Wilson";
	setAttr ".cdat" -type "string" "2012/09/09 19:57:03";
	setAttr ".te" -type "string" "NWHingeJoints";
	setAttr ".ia" -type "stringArray" 4 "type" "trans" "attr" ""  ;
	setAttr ".re" -type "stringArray" 6 "input_root" "regBlueprintTransform" "regBlueprintShape" "regRigTransform" "regRigShape" "connection_endControl_root_data"  ;
	setAttr ".sj" -type "stringArray" 3 "NWHingeJointsBaseBlueprinter_SJNT" "NWHingeJointsMiddleBlueprinter_SJNT" "NWHingeJointsEndBlueprinter_SJNT"  ;
	setAttr ".sc" -type "stringArray" 3 "NWHingeJointsBaseBlueprinter_SCTL" "NWHingeJointsMiddleBlueprinter_SCTL" "NWHingeJointsEndBlueprinter_SCTL"  ;
	setAttr ".st" 1;
	setAttr ".bu" 1;
	setAttr ".ca" -type "stringArray" 10 "type:" "trans" "attr:" "None" "input:" "NWHingeJoints.root" "output:" "NWSpineJoints.endControl" "connectionKey:" "endControl_root"  ;
createNode hyperLayout -n "hyperLayout3";
	setAttr ".ihi" 0;
	setAttr -s 73 ".hyp";
createNode polySphere -n "polySphere6";
	setAttr ".r" 0.5;
	setAttr ".sa" 1;
	setAttr ".sh" 1;
createNode polyCube -n "polyCube1";
	setAttr ".cuv" 4;
createNode polySphere -n "polySphere7";
	setAttr ".r" 0.5;
	setAttr ".sa" 1;
	setAttr ".sh" 1;
createNode multDoubleLinear -n "NWHingeJointsaxisCtlX_PMA";
	setAttr ".i2" -1;
createNode multDoubleLinear -n "NWHingeJointsaxisCtlY_PMA";
	setAttr ".i2" -1;
createNode multDoubleLinear -n "NWHingeJointsaxisCtlZ_PMA";
	setAttr ".i2" -1;
createNode ikRPsolver -n "ikRPsolver";
createNode ikSplineSolver -n "ikSplineSolver";
createNode cluster -n "NWSpineJointsIKCluster0_CLS";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak1";
createNode objectSet -n "NWSpineJointsIKCluster0_CLSSet";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "NWSpineJointsIKCluster0_CLSGroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "NWSpineJointsIKCluster0_CLSGroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0]";
createNode objectSet -n "tweakSet1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "NWSpineJointsIKCluster1_CLS";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "NWSpineJointsIKCluster1_CLSSet";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "NWSpineJointsIKCluster1_CLSGroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "NWSpineJointsIKCluster1_CLSGroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode cluster -n "NWSpineJointsIKCluster2_CLS";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "NWSpineJointsIKCluster2_CLSSet";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "NWSpineJointsIKCluster2_CLSGroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "NWSpineJointsIKCluster2_CLSGroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[2]";
createNode cluster -n "NWSpineJointsIKCluster3_CLS";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "NWSpineJointsIKCluster3_CLSSet";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "NWSpineJointsIKCluster3_CLSGroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "NWSpineJointsIKCluster3_CLSGroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[3]";
createNode makeNurbCircle -n "makeNurbCircle1";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle2";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle3";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle4";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle5";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n"
		+ "                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n"
		+ "            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n"
		+ "            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -shadows 0\n"
		+ "            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n"
		+ "                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n"
		+ "                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n"
		+ "                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n"
		+ "            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n"
		+ "            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n"
		+ "                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n"
		+ "                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n"
		+ "                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n"
		+ "            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n"
		+ "            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n"
		+ "            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 8192\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n"
		+ "                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n"
		+ "                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n"
		+ "            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 8192\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n"
		+ "            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -showShapes 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n"
		+ "                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 0\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\toutlinerPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n"
		+ "                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n"
		+ "                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n"
		+ "                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n"
		+ "                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n"
		+ "                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n"
		+ "                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n"
		+ "                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n"
		+ "                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n"
		+ "                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n"
		+ "                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n"
		+ "                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n"
		+ "                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xpm\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 8192\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 8192\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 24 -ast 1 -aet 48 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :initialShadingGroup;
	setAttr -s 8 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :renderGlobalsList1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
select -ne :ikSystem;
	setAttr -s 2 ".sol";
connectAttr "nwRig_CNT.input_root" "nwRigRoot_GRP.input_root";
connectAttr "NWSpineJoints_CNT.input_root" "NWSpineJointsRoot_GRP.input_root";
connectAttr "NWSpineJointsSpineChainBlueprinter0_PNT.ctx" "NWSpineJointsSpineChainBlueprinter0_SJNT.tx"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_PNT.cty" "NWSpineJointsSpineChainBlueprinter0_SJNT.ty"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_PNT.ctz" "NWSpineJointsSpineChainBlueprinter0_SJNT.tz"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SJNT.pim" "NWSpineJointsSpineChainBlueprinter0_PNT.cpim"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SJNT.rp" "NWSpineJointsSpineChainBlueprinter0_PNT.crp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SJNT.rpt" "NWSpineJointsSpineChainBlueprinter0_PNT.crt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SCTL.t" "NWSpineJointsSpineChainBlueprinter0_PNT.tg[0].tt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SCTL.rp" "NWSpineJointsSpineChainBlueprinter0_PNT.tg[0].trp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SCTL.rpt" "NWSpineJointsSpineChainBlueprinter0_PNT.tg[0].trt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SCTL.pm" "NWSpineJointsSpineChainBlueprinter0_PNT.tg[0].tpm"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_PNT.w0" "NWSpineJointsSpineChainBlueprinter0_PNT.tg[0].tw"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_PNT.ctx" "NWSpineJointsSpineChainBlueprinter1_SJNT.tx"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_PNT.cty" "NWSpineJointsSpineChainBlueprinter1_SJNT.ty"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_PNT.ctz" "NWSpineJointsSpineChainBlueprinter1_SJNT.tz"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SJNT.s" "NWSpineJointsSpineChainBlueprinter1_SJNT.is"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SJNT.pim" "NWSpineJointsSpineChainBlueprinter1_PNT.cpim"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SJNT.rp" "NWSpineJointsSpineChainBlueprinter1_PNT.crp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SJNT.rpt" "NWSpineJointsSpineChainBlueprinter1_PNT.crt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SCTL.t" "NWSpineJointsSpineChainBlueprinter1_PNT.tg[0].tt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SCTL.rp" "NWSpineJointsSpineChainBlueprinter1_PNT.tg[0].trp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SCTL.rpt" "NWSpineJointsSpineChainBlueprinter1_PNT.tg[0].trt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SCTL.pm" "NWSpineJointsSpineChainBlueprinter1_PNT.tg[0].tpm"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_PNT.w0" "NWSpineJointsSpineChainBlueprinter1_PNT.tg[0].tw"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_PNT.ctx" "NWSpineJointsSpineChainBlueprinter2_SJNT.tx"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_PNT.cty" "NWSpineJointsSpineChainBlueprinter2_SJNT.ty"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_PNT.ctz" "NWSpineJointsSpineChainBlueprinter2_SJNT.tz"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SJNT.s" "NWSpineJointsSpineChainBlueprinter2_SJNT.is"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SJNT.pim" "NWSpineJointsSpineChainBlueprinter2_PNT.cpim"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SJNT.rp" "NWSpineJointsSpineChainBlueprinter2_PNT.crp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SJNT.rpt" "NWSpineJointsSpineChainBlueprinter2_PNT.crt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SCTL.t" "NWSpineJointsSpineChainBlueprinter2_PNT.tg[0].tt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SCTL.rp" "NWSpineJointsSpineChainBlueprinter2_PNT.tg[0].trp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SCTL.rpt" "NWSpineJointsSpineChainBlueprinter2_PNT.tg[0].trt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SCTL.pm" "NWSpineJointsSpineChainBlueprinter2_PNT.tg[0].tpm"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_PNT.w0" "NWSpineJointsSpineChainBlueprinter2_PNT.tg[0].tw"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_PNT.ctx" "NWSpineJointsSpineChainBlueprinter3_SJNT.tx"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_PNT.cty" "NWSpineJointsSpineChainBlueprinter3_SJNT.ty"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_PNT.ctz" "NWSpineJointsSpineChainBlueprinter3_SJNT.tz"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SJNT.s" "NWSpineJointsSpineChainBlueprinter3_SJNT.is"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SJNT.pim" "NWSpineJointsSpineChainBlueprinter3_PNT.cpim"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SJNT.rp" "NWSpineJointsSpineChainBlueprinter3_PNT.crp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SJNT.rpt" "NWSpineJointsSpineChainBlueprinter3_PNT.crt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SCTL.t" "NWSpineJointsSpineChainBlueprinter3_PNT.tg[0].tt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SCTL.rp" "NWSpineJointsSpineChainBlueprinter3_PNT.tg[0].trp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SCTL.rpt" "NWSpineJointsSpineChainBlueprinter3_PNT.tg[0].trt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SCTL.pm" "NWSpineJointsSpineChainBlueprinter3_PNT.tg[0].tpm"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_PNT.w0" "NWSpineJointsSpineChainBlueprinter3_PNT.tg[0].tw"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_PNT.ctx" "NWSpineJointsSpineChainBlueprinter4_SJNT.tx"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_PNT.cty" "NWSpineJointsSpineChainBlueprinter4_SJNT.ty"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_PNT.ctz" "NWSpineJointsSpineChainBlueprinter4_SJNT.tz"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SJNT.s" "NWSpineJointsSpineChainBlueprinter4_SJNT.is"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SJNT.pim" "NWSpineJointsSpineChainBlueprinter4_PNT.cpim"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SJNT.rp" "NWSpineJointsSpineChainBlueprinter4_PNT.crp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SJNT.rpt" "NWSpineJointsSpineChainBlueprinter4_PNT.crt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SCTL.t" "NWSpineJointsSpineChainBlueprinter4_PNT.tg[0].tt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SCTL.rp" "NWSpineJointsSpineChainBlueprinter4_PNT.tg[0].trp"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SCTL.rpt" "NWSpineJointsSpineChainBlueprinter4_PNT.tg[0].trt"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SCTL.pm" "NWSpineJointsSpineChainBlueprinter4_PNT.tg[0].tpm"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_PNT.w0" "NWSpineJointsSpineChainBlueprinter4_PNT.tg[0].tw"
		;
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter0Sctl_GRP.regBlueprintTransform"
		;
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter0_SCTL.regBlueprintTransform"
		;
connectAttr "polySphere1.out" "NWSpineJointsSpineChainBlueprinter0_SCTLShape.i";
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter1Sctl_GRP.regBlueprintTransform"
		;
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter1_SCTL.regBlueprintTransform"
		;
connectAttr "polySphere2.out" "NWSpineJointsSpineChainBlueprinter1_SCTLShape.i";
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter2Sctl_GRP.regBlueprintTransform"
		;
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter2_SCTL.regBlueprintTransform"
		;
connectAttr "polySphere3.out" "NWSpineJointsSpineChainBlueprinter2_SCTLShape.i";
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter3Sctl_GRP.regBlueprintTransform"
		;
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter3_SCTL.regBlueprintTransform"
		;
connectAttr "polySphere4.out" "NWSpineJointsSpineChainBlueprinter3_SCTLShape.i";
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter4Sctl_GRP.regBlueprintTransform"
		;
connectAttr "NWSpineJoints_CNT.regBlueprintTransform" "NWSpineJointsSpineChainBlueprinter4_SCTL.regBlueprintTransform"
		;
connectAttr "polySphere5.out" "NWSpineJointsSpineChainBlueprinter4_SCTLShape.i";
connectAttr "NWSpineJoints5_JNT.tx" "effector1.tx";
connectAttr "NWSpineJoints5_JNT.ty" "effector1.ty";
connectAttr "NWSpineJoints5_JNT.tz" "effector1.tz";
connectAttr "NWSpineJointsIKCluster3_CLS.og[0]" "NWSpineJointsIK_CRVShape.cr";
connectAttr "tweak1.pl[0].cp[0]" "NWSpineJointsIK_CRVShape.twl";
connectAttr "NWSpineJointsIKCluster0_CLSGroupId.id" "NWSpineJointsIK_CRVShape.iog.og[0].gid"
		;
connectAttr "NWSpineJointsIKCluster0_CLSSet.mwc" "NWSpineJointsIK_CRVShape.iog.og[0].gco"
		;
connectAttr "groupId2.id" "NWSpineJointsIK_CRVShape.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "NWSpineJointsIK_CRVShape.iog.og[1].gco";
connectAttr "NWSpineJointsIKCluster1_CLSGroupId.id" "NWSpineJointsIK_CRVShape.iog.og[2].gid"
		;
connectAttr "NWSpineJointsIKCluster1_CLSSet.mwc" "NWSpineJointsIK_CRVShape.iog.og[2].gco"
		;
connectAttr "NWSpineJointsIKCluster2_CLSGroupId.id" "NWSpineJointsIK_CRVShape.iog.og[3].gid"
		;
connectAttr "NWSpineJointsIKCluster2_CLSSet.mwc" "NWSpineJointsIK_CRVShape.iog.og[3].gco"
		;
connectAttr "NWSpineJointsIKCluster3_CLSGroupId.id" "NWSpineJointsIK_CRVShape.iog.og[4].gid"
		;
connectAttr "NWSpineJointsIKCluster3_CLSSet.mwc" "NWSpineJointsIK_CRVShape.iog.og[4].gco"
		;
connectAttr "NWSpineJoints1_JNT.msg" "NWSpineJoints_IKH.hsj";
connectAttr "effector1.hp" "NWSpineJoints_IKH.hee";
connectAttr "ikSplineSolver.msg" "NWSpineJoints_IKH.hsv";
connectAttr "NWSpineJointsIK_CRVShape.ws" "NWSpineJoints_IKH.ic";
connectAttr "makeNurbCircle1.oc" "NWSpineJointsIKCluster0_CTLShape.cr";
connectAttr "makeNurbCircle2.oc" "NWSpineJointsIKCluster1_CTLShape.cr";
connectAttr "makeNurbCircle3.oc" "NWSpineJointsIKCluster2_CTLShape.cr";
connectAttr "NWSpineJoints_CNT.output_endControl" "NWSpineJointsIKCluster3_CTL.output_endControl"
		;
connectAttr "makeNurbCircle4.oc" "NWSpineJointsIKCluster3_CTLShape.cr";
connectAttr "NWHingeJoints_CNT.input_root" "NWHingeJointsRoot_GRP.input_root";
connectAttr "NWHingeJointsRoot_GRP_parentConstraint1.ctx" "NWHingeJointsRoot_GRP.tx"
		;
connectAttr "NWHingeJointsRoot_GRP_parentConstraint1.cty" "NWHingeJointsRoot_GRP.ty"
		;
connectAttr "NWHingeJointsRoot_GRP_parentConstraint1.ctz" "NWHingeJointsRoot_GRP.tz"
		;
connectAttr "NWHingeJointsRoot_GRP_parentConstraint1.crx" "NWHingeJointsRoot_GRP.rx"
		;
connectAttr "NWHingeJointsRoot_GRP_parentConstraint1.cry" "NWHingeJointsRoot_GRP.ry"
		;
connectAttr "NWHingeJointsRoot_GRP_parentConstraint1.crz" "NWHingeJointsRoot_GRP.rz"
		;
connectAttr "NWHingeJointsBaseBlueprinter_PNT.ctx" "NWHingeJointsBaseBlueprinter_SJNT.tx"
		;
connectAttr "NWHingeJointsBaseBlueprinter_PNT.cty" "NWHingeJointsBaseBlueprinter_SJNT.ty"
		;
connectAttr "NWHingeJointsBaseBlueprinter_PNT.ctz" "NWHingeJointsBaseBlueprinter_SJNT.tz"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SJNT.pim" "NWHingeJointsBaseBlueprinter_PNT.cpim"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SJNT.rp" "NWHingeJointsBaseBlueprinter_PNT.crp"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SJNT.rpt" "NWHingeJointsBaseBlueprinter_PNT.crt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.t" "NWHingeJointsBaseBlueprinter_PNT.tg[0].tt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rp" "NWHingeJointsBaseBlueprinter_PNT.tg[0].trp"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rpt" "NWHingeJointsBaseBlueprinter_PNT.tg[0].trt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.pm" "NWHingeJointsBaseBlueprinter_PNT.tg[0].tpm"
		;
connectAttr "NWHingeJointsBaseBlueprinter_PNT.w0" "NWHingeJointsBaseBlueprinter_PNT.tg[0].tw"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_PNT.ctx" "NWHingeJointsMiddleBlueprinter_SJNT.tx"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_PNT.cty" "NWHingeJointsMiddleBlueprinter_SJNT.ty"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_PNT.ctz" "NWHingeJointsMiddleBlueprinter_SJNT.tz"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SJNT.s" "NWHingeJointsMiddleBlueprinter_SJNT.is"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SJNT.pim" "NWHingeJointsMiddleBlueprinter_PNT.cpim"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SJNT.rp" "NWHingeJointsMiddleBlueprinter_PNT.crp"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SJNT.rpt" "NWHingeJointsMiddleBlueprinter_PNT.crt"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SCTL.t" "NWHingeJointsMiddleBlueprinter_PNT.tg[0].tt"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SCTL.rp" "NWHingeJointsMiddleBlueprinter_PNT.tg[0].trp"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SCTL.rpt" "NWHingeJointsMiddleBlueprinter_PNT.tg[0].trt"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SCTL.pm" "NWHingeJointsMiddleBlueprinter_PNT.tg[0].tpm"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_PNT.w0" "NWHingeJointsMiddleBlueprinter_PNT.tg[0].tw"
		;
connectAttr "NWHingeJointsEndBlueprinter_PNT.ctx" "NWHingeJointsEndBlueprinter_SJNT.tx"
		;
connectAttr "NWHingeJointsEndBlueprinter_PNT.cty" "NWHingeJointsEndBlueprinter_SJNT.ty"
		;
connectAttr "NWHingeJointsEndBlueprinter_PNT.ctz" "NWHingeJointsEndBlueprinter_SJNT.tz"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SJNT.s" "NWHingeJointsEndBlueprinter_SJNT.is"
		;
connectAttr "NWHingeJointsEndBlueprinter_SJNT.pim" "NWHingeJointsEndBlueprinter_PNT.cpim"
		;
connectAttr "NWHingeJointsEndBlueprinter_SJNT.rp" "NWHingeJointsEndBlueprinter_PNT.crp"
		;
connectAttr "NWHingeJointsEndBlueprinter_SJNT.rpt" "NWHingeJointsEndBlueprinter_PNT.crt"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.t" "NWHingeJointsEndBlueprinter_PNT.tg[0].tt"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.rp" "NWHingeJointsEndBlueprinter_PNT.tg[0].trp"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.rpt" "NWHingeJointsEndBlueprinter_PNT.tg[0].trt"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.pm" "NWHingeJointsEndBlueprinter_PNT.tg[0].tpm"
		;
connectAttr "NWHingeJointsEndBlueprinter_PNT.w0" "NWHingeJointsEndBlueprinter_PNT.tg[0].tw"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsBaseBlueprinterSctl_GRP.regBlueprintTransform"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsBaseBlueprinter_SCTL.regBlueprintTransform"
		;
connectAttr "polySphere6.out" "NWHingeJointsBaseBlueprinter_SCTLShape.i";
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsEndBlueprinterSctl_GRP.regBlueprintTransform"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsEndBlueprinter_SCTL.regBlueprintTransform"
		;
connectAttr "polySphere7.out" "NWHingeJointsEndBlueprinter_SCTLShape.i";
connectAttr "NWHingeJointsBaseEndConst_PNT.ctx" "NWHingeJointsaxisCtl_GRP.tx";
connectAttr "NWHingeJointsBaseEndConst_PNT.cty" "NWHingeJointsaxisCtl_GRP.ty";
connectAttr "NWHingeJointsBaseEndConst_PNT.ctz" "NWHingeJointsaxisCtl_GRP.tz";
connectAttr "NWHingeJointsBaseEndConst_AIM.crx" "NWHingeJointsaxisCtl_GRP.rx";
connectAttr "NWHingeJointsBaseEndConst_AIM.cry" "NWHingeJointsaxisCtl_GRP.ry";
connectAttr "NWHingeJointsBaseEndConst_AIM.crz" "NWHingeJointsaxisCtl_GRP.rz";
connectAttr "NWHingeJointsaxisCtlX_CTL.tx" "NWHingeJointsaxisCtlCtl_GRP.tx";
connectAttr "NWHingeJointsaxisCtlY_CTL.ty" "NWHingeJointsaxisCtlCtl_GRP.ty";
connectAttr "NWHingeJointsaxisCtlZ_CTL.tz" "NWHingeJointsaxisCtlCtl_GRP.tz";
connectAttr "NWHingeJointsaxisCtlX_PMA.o" "NWHingeJointsaxisCtlXCtl_GRP.tx";
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsaxisCtlXCtl_GRP.regBlueprintTransform"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsaxisCtlX_CTL.regBlueprintTransform"
		;
connectAttr "NWHingeJointsaxisCtlY_PMA.o" "NWHingeJointsaxisCtlYCtl_GRP.ty";
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsaxisCtlYCtl_GRP.regBlueprintTransform"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsaxisCtlY_CTL.regBlueprintTransform"
		;
connectAttr "NWHingeJointsaxisCtlZ_PMA.o" "NWHingeJointsaxisCtlZCtl_GRP.tz";
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsaxisCtlZCtl_GRP.regBlueprintTransform"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsaxisCtlZ_CTL.regBlueprintTransform"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsMiddleBlueprinterSctl_GRP.regBlueprintTransform"
		;
connectAttr "NWHingeJoints_CNT.regBlueprintTransform" "NWHingeJointsMiddleBlueprinter_SCTL.regBlueprintTransform"
		;
connectAttr "polyCube1.out" "NWHingeJointsMiddleBlueprinter_SCTLShape.i";
connectAttr "NWHingeJointsaxisCtl_GRP.pim" "NWHingeJointsBaseEndConst_PNT.cpim";
connectAttr "NWHingeJointsaxisCtl_GRP.rp" "NWHingeJointsBaseEndConst_PNT.crp";
connectAttr "NWHingeJointsaxisCtl_GRP.rpt" "NWHingeJointsBaseEndConst_PNT.crt";
connectAttr "NWHingeJointsEndBlueprinter_SCTL.t" "NWHingeJointsBaseEndConst_PNT.tg[0].tt"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.rp" "NWHingeJointsBaseEndConst_PNT.tg[0].trp"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.rpt" "NWHingeJointsBaseEndConst_PNT.tg[0].trt"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.pm" "NWHingeJointsBaseEndConst_PNT.tg[0].tpm"
		;
connectAttr "NWHingeJointsBaseEndConst_PNT.w0" "NWHingeJointsBaseEndConst_PNT.tg[0].tw"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.t" "NWHingeJointsBaseEndConst_PNT.tg[1].tt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rp" "NWHingeJointsBaseEndConst_PNT.tg[1].trp"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rpt" "NWHingeJointsBaseEndConst_PNT.tg[1].trt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.pm" "NWHingeJointsBaseEndConst_PNT.tg[1].tpm"
		;
connectAttr "NWHingeJointsBaseEndConst_PNT.w1" "NWHingeJointsBaseEndConst_PNT.tg[1].tw"
		;
connectAttr "NWHingeJointsaxisCtl_GRP.pim" "NWHingeJointsBaseEndConst_AIM.cpim";
connectAttr "NWHingeJointsaxisCtl_GRP.t" "NWHingeJointsBaseEndConst_AIM.ct";
connectAttr "NWHingeJointsaxisCtl_GRP.rp" "NWHingeJointsBaseEndConst_AIM.crp";
connectAttr "NWHingeJointsaxisCtl_GRP.rpt" "NWHingeJointsBaseEndConst_AIM.crt";
connectAttr "NWHingeJointsaxisCtl_GRP.ro" "NWHingeJointsBaseEndConst_AIM.cro";
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.t" "NWHingeJointsBaseEndConst_AIM.tg[0].tt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rp" "NWHingeJointsBaseEndConst_AIM.tg[0].trp"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rpt" "NWHingeJointsBaseEndConst_AIM.tg[0].trt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.pm" "NWHingeJointsBaseEndConst_AIM.tg[0].tpm"
		;
connectAttr "NWHingeJointsBaseEndConst_AIM.w0" "NWHingeJointsBaseEndConst_AIM.tg[0].tw"
		;
connectAttr "NWHingeJointsArrowConst_PNT.ctx" "NWHingeJointsDirectionSctl_GRP.tx"
		;
connectAttr "NWHingeJointsArrowConst_PNT.cty" "NWHingeJointsDirectionSctl_GRP.ty"
		;
connectAttr "NWHingeJointsArrowConst_PNT.ctz" "NWHingeJointsDirectionSctl_GRP.tz"
		;
connectAttr "NWHingeJointsArrowConst_AIM.crx" "NWHingeJointsDirectionSctl_GRP.rx"
		;
connectAttr "NWHingeJointsArrowConst_AIM.cry" "NWHingeJointsDirectionSctl_GRP.ry"
		;
connectAttr "NWHingeJointsArrowConst_AIM.crz" "NWHingeJointsDirectionSctl_GRP.rz"
		;
connectAttr "NWHingeJointsDirection_PNT.ctx" "NWHingeJointsDirection_SJNT.tx";
connectAttr "NWHingeJointsDirection_PNT.cty" "NWHingeJointsDirection_SJNT.ty";
connectAttr "NWHingeJointsDirection_PNT.ctz" "NWHingeJointsDirection_SJNT.tz";
connectAttr "NWHingeJointsDirection_SJNT.pim" "NWHingeJointsDirection_PNT.cpim";
connectAttr "NWHingeJointsDirection_SJNT.rp" "NWHingeJointsDirection_PNT.crp";
connectAttr "NWHingeJointsDirection_SJNT.rpt" "NWHingeJointsDirection_PNT.crt";
connectAttr "NWHingeJointsDirection_SCTL.t" "NWHingeJointsDirection_PNT.tg[0].tt"
		;
connectAttr "NWHingeJointsDirection_SCTL.rp" "NWHingeJointsDirection_PNT.tg[0].trp"
		;
connectAttr "NWHingeJointsDirection_SCTL.rpt" "NWHingeJointsDirection_PNT.tg[0].trt"
		;
connectAttr "NWHingeJointsDirection_SCTL.pm" "NWHingeJointsDirection_PNT.tg[0].tpm"
		;
connectAttr "NWHingeJointsDirection_PNT.w0" "NWHingeJointsDirection_PNT.tg[0].tw"
		;
connectAttr "NWHingeJointsDirectionSctl_GRP.pim" "NWHingeJointsArrowConst_PNT.cpim"
		;
connectAttr "NWHingeJointsDirectionSctl_GRP.rp" "NWHingeJointsArrowConst_PNT.crp"
		;
connectAttr "NWHingeJointsDirectionSctl_GRP.rpt" "NWHingeJointsArrowConst_PNT.crt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.t" "NWHingeJointsArrowConst_PNT.tg[0].tt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rp" "NWHingeJointsArrowConst_PNT.tg[0].trp"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.rpt" "NWHingeJointsArrowConst_PNT.tg[0].trt"
		;
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.pm" "NWHingeJointsArrowConst_PNT.tg[0].tpm"
		;
connectAttr "NWHingeJointsArrowConst_PNT.w0" "NWHingeJointsArrowConst_PNT.tg[0].tw"
		;
connectAttr "NWHingeJointsDirectionSctl_GRP.pim" "NWHingeJointsArrowConst_AIM.cpim"
		;
connectAttr "NWHingeJointsDirectionSctl_GRP.t" "NWHingeJointsArrowConst_AIM.ct";
connectAttr "NWHingeJointsDirectionSctl_GRP.rp" "NWHingeJointsArrowConst_AIM.crp"
		;
connectAttr "NWHingeJointsDirectionSctl_GRP.rpt" "NWHingeJointsArrowConst_AIM.crt"
		;
connectAttr "NWHingeJointsDirectionSctl_GRP.ro" "NWHingeJointsArrowConst_AIM.cro"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.t" "NWHingeJointsArrowConst_AIM.tg[0].tt"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.rp" "NWHingeJointsArrowConst_AIM.tg[0].trp"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.rpt" "NWHingeJointsArrowConst_AIM.tg[0].trt"
		;
connectAttr "NWHingeJointsEndBlueprinter_SCTL.pm" "NWHingeJointsArrowConst_AIM.tg[0].tpm"
		;
connectAttr "NWHingeJointsArrowConst_AIM.w0" "NWHingeJointsArrowConst_AIM.tg[0].tw"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.ctx" "NWHingeJoints1_JNT.tx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.cty" "NWHingeJoints1_JNT.ty"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.ctz" "NWHingeJoints1_JNT.tz"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.crx" "NWHingeJoints1_JNT.rx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.cry" "NWHingeJoints1_JNT.ry"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.crz" "NWHingeJoints1_JNT.rz"
		;
connectAttr "NWHingeJoints3_JNT.tx" "effector2.tx";
connectAttr "NWHingeJoints3_JNT.ty" "effector2.ty";
connectAttr "NWHingeJoints3_JNT.tz" "effector2.tz";
connectAttr "NWHingeJoints1_JNT.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.cro"
		;
connectAttr "NWHingeJoints1_JNT.pim" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.cpim"
		;
connectAttr "NWHingeJoints1_JNT.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.crp"
		;
connectAttr "NWHingeJoints1_JNT.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.crt"
		;
connectAttr "NWHingeJoints1_JNT.jo" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.cjo"
		;
connectAttr "NWHingeJointsBase_CTL.t" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].tt"
		;
connectAttr "NWHingeJointsBase_CTL.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].trp"
		;
connectAttr "NWHingeJointsBase_CTL.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].trt"
		;
connectAttr "NWHingeJointsBase_CTL.r" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].tr"
		;
connectAttr "NWHingeJointsBase_CTL.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].tro"
		;
connectAttr "NWHingeJointsBase_CTL.s" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].ts"
		;
connectAttr "NWHingeJointsBase_CTL.pm" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].tpm"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.w0" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.tg[0].tw"
		;
connectAttr "NWHingeJoints1_JNT.msg" "NWHingeJoints_IKH.hsj";
connectAttr "effector2.hp" "NWHingeJoints_IKH.hee";
connectAttr "ikRPsolver.msg" "NWHingeJoints_IKH.hsv";
connectAttr "NWHingeJointsPole_PVC.ctx" "NWHingeJoints_IKH.pvx";
connectAttr "NWHingeJointsPole_PVC.cty" "NWHingeJoints_IKH.pvy";
connectAttr "NWHingeJointsPole_PVC.ctz" "NWHingeJoints_IKH.pvz";
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.ctx" "NWHingeJoints_IKH.tx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.cty" "NWHingeJoints_IKH.ty"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.ctz" "NWHingeJoints_IKH.tz"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.crx" "NWHingeJoints_IKH.rx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.cry" "NWHingeJoints_IKH.ry"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.crz" "NWHingeJoints_IKH.rz"
		;
connectAttr "NWHingeJoints_IKH.pim" "NWHingeJointsPole_PVC.cpim";
connectAttr "NWHingeJoints1_JNT.pm" "NWHingeJointsPole_PVC.ps";
connectAttr "NWHingeJoints1_JNT.t" "NWHingeJointsPole_PVC.crp";
connectAttr "NWHingeJointsPole_LOC.t" "NWHingeJointsPole_PVC.tg[0].tt";
connectAttr "NWHingeJointsPole_LOC.rp" "NWHingeJointsPole_PVC.tg[0].trp";
connectAttr "NWHingeJointsPole_LOC.rpt" "NWHingeJointsPole_PVC.tg[0].trt";
connectAttr "NWHingeJointsPole_LOC.pm" "NWHingeJointsPole_PVC.tg[0].tpm";
connectAttr "NWHingeJointsPole_PVC.w0" "NWHingeJointsPole_PVC.tg[0].tw";
connectAttr "NWHingeJoints_IKH.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.cro"
		;
connectAttr "NWHingeJoints_IKH.pim" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.cpim"
		;
connectAttr "NWHingeJoints_IKH.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.crp"
		;
connectAttr "NWHingeJoints_IKH.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.crt"
		;
connectAttr "NWHingeJointsIK_CTL.t" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].tt"
		;
connectAttr "NWHingeJointsIK_CTL.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].trp"
		;
connectAttr "NWHingeJointsIK_CTL.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].trt"
		;
connectAttr "NWHingeJointsIK_CTL.r" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].tr"
		;
connectAttr "NWHingeJointsIK_CTL.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].tro"
		;
connectAttr "NWHingeJointsIK_CTL.s" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].ts"
		;
connectAttr "NWHingeJointsIK_CTL.pm" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].tpm"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.w0" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.tg[0].tw"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.ctx" "NWHingeJointsPole_GRP.tx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.cty" "NWHingeJointsPole_GRP.ty"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.ctz" "NWHingeJointsPole_GRP.tz"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.crx" "NWHingeJointsPole_GRP.rx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.cry" "NWHingeJointsPole_GRP.ry"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.crz" "NWHingeJointsPole_GRP.rz"
		;
connectAttr "NWHingeJointsPole_GRP.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.cro"
		;
connectAttr "NWHingeJointsPole_GRP.pim" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.cpim"
		;
connectAttr "NWHingeJointsPole_GRP.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.crp"
		;
connectAttr "NWHingeJointsPole_GRP.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.crt"
		;
connectAttr "NWHingeJointsPole_CTL.t" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].tt"
		;
connectAttr "NWHingeJointsPole_CTL.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].trp"
		;
connectAttr "NWHingeJointsPole_CTL.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].trt"
		;
connectAttr "NWHingeJointsPole_CTL.r" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].tr"
		;
connectAttr "NWHingeJointsPole_CTL.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].tro"
		;
connectAttr "NWHingeJointsPole_CTL.s" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].ts"
		;
connectAttr "NWHingeJointsPole_CTL.pm" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].tpm"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.w0" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.tg[0].tw"
		;
connectAttr "NWHingeJoints_CNT.regRigTransform" "NWHingeJointsBaseCtl_GRP.regRigTransform"
		;
connectAttr "NWHingeJoints_CNT.regRigTransform" "NWHingeJointsBase_CTL.regRigTransform"
		;
connectAttr "makeNurbCircle5.oc" "NWHingeJointsBase_CTLShape.cr";
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.ctx" "NWHingeJointsIKCtl_GRP.tx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.cty" "NWHingeJointsIKCtl_GRP.ty"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.ctz" "NWHingeJointsIKCtl_GRP.tz"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.crx" "NWHingeJointsIKCtl_GRP.rx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.cry" "NWHingeJointsIKCtl_GRP.ry"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.crz" "NWHingeJointsIKCtl_GRP.rz"
		;
connectAttr "NWHingeJoints_CNT.regRigTransform" "NWHingeJointsIKCtl_GRP.regRigTransform"
		;
connectAttr "NWHingeJoints_CNT.regRigTransform" "NWHingeJointsIK_CTL.regRigTransform"
		;
connectAttr "NWHingeJointsIKCtl_GRP.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.cro"
		;
connectAttr "NWHingeJointsIKCtl_GRP.pim" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.cpim"
		;
connectAttr "NWHingeJointsIKCtl_GRP.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.crp"
		;
connectAttr "NWHingeJointsIKCtl_GRP.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.crt"
		;
connectAttr "NWHingeJointsBase_CTL.t" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].tt"
		;
connectAttr "NWHingeJointsBase_CTL.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].trp"
		;
connectAttr "NWHingeJointsBase_CTL.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].trt"
		;
connectAttr "NWHingeJointsBase_CTL.r" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].tr"
		;
connectAttr "NWHingeJointsBase_CTL.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].tro"
		;
connectAttr "NWHingeJointsBase_CTL.s" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].ts"
		;
connectAttr "NWHingeJointsBase_CTL.pm" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].tpm"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.w0" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.tg[0].tw"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.ctx" "NWHingeJointsPoleCtl_GRP.tx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.cty" "NWHingeJointsPoleCtl_GRP.ty"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.ctz" "NWHingeJointsPoleCtl_GRP.tz"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.crx" "NWHingeJointsPoleCtl_GRP.rx"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.cry" "NWHingeJointsPoleCtl_GRP.ry"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.crz" "NWHingeJointsPoleCtl_GRP.rz"
		;
connectAttr "NWHingeJoints_CNT.regRigTransform" "NWHingeJointsPoleCtl_GRP.regRigTransform"
		;
connectAttr "NWHingeJoints_CNT.regRigTransform" "NWHingeJointsPole_CTL.regRigTransform"
		;
connectAttr "NWHingeJointsPoleCtl_GRP.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.cro"
		;
connectAttr "NWHingeJointsPoleCtl_GRP.pim" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.cpim"
		;
connectAttr "NWHingeJointsPoleCtl_GRP.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.crp"
		;
connectAttr "NWHingeJointsPoleCtl_GRP.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.crt"
		;
connectAttr "NWHingeJointsBase_CTL.t" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].tt"
		;
connectAttr "NWHingeJointsBase_CTL.rp" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].trp"
		;
connectAttr "NWHingeJointsBase_CTL.rpt" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].trt"
		;
connectAttr "NWHingeJointsBase_CTL.r" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].tr"
		;
connectAttr "NWHingeJointsBase_CTL.ro" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].tro"
		;
connectAttr "NWHingeJointsBase_CTL.s" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].ts"
		;
connectAttr "NWHingeJointsBase_CTL.pm" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].tpm"
		;
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.w0" "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.tg[0].tw"
		;
connectAttr "NWHingeJointsRoot_GRP.ro" "NWHingeJointsRoot_GRP_parentConstraint1.cro"
		;
connectAttr "NWHingeJointsRoot_GRP.pim" "NWHingeJointsRoot_GRP_parentConstraint1.cpim"
		;
connectAttr "NWHingeJointsRoot_GRP.rp" "NWHingeJointsRoot_GRP_parentConstraint1.crp"
		;
connectAttr "NWHingeJointsRoot_GRP.rpt" "NWHingeJointsRoot_GRP_parentConstraint1.crt"
		;
connectAttr "NWSpineJointsIKCluster3_CTL.t" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].tt"
		;
connectAttr "NWSpineJointsIKCluster3_CTL.rp" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].trp"
		;
connectAttr "NWSpineJointsIKCluster3_CTL.rpt" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].trt"
		;
connectAttr "NWSpineJointsIKCluster3_CTL.r" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].tr"
		;
connectAttr "NWSpineJointsIKCluster3_CTL.ro" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].tro"
		;
connectAttr "NWSpineJointsIKCluster3_CTL.s" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].ts"
		;
connectAttr "NWSpineJointsIKCluster3_CTL.pm" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].tpm"
		;
connectAttr "NWHingeJointsRoot_GRP_parentConstraint1.w0" "NWHingeJointsRoot_GRP_parentConstraint1.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "hyperLayout1.msg" "nwRig_CNT.hl";
connectAttr "nwRigRoot_GRP.msg" "hyperLayout1.hyp[0].dn";
connectAttr "modules_GRP.msg" "hyperLayout1.hyp[1].dn";
connectAttr "geometry_GRP.msg" "hyperLayout1.hyp[2].dn";
connectAttr "global_GRP.msg" "hyperLayout1.hyp[3].dn";
connectAttr "NWSpineJoints_CNT.msg" "hyperLayout1.hyp[4].dn";
connectAttr "NWHingeJoints_CNT.msg" "hyperLayout1.hyp[5].dn";
connectAttr "hyperLayout2.msg" "NWSpineJoints_CNT.hl";
connectAttr "NWSpineJointsRoot_GRP.msg" "hyperLayout2.hyp[0].dn";
connectAttr "NWSpineJointsBlueprint_GRP.msg" "hyperLayout2.hyp[1].dn";
connectAttr "NWSpineJointsBlueprintJoint_GRP.msg" "hyperLayout2.hyp[2].dn";
connectAttr "NWSpineJointsSpineChainBlueprinter0_SJNT.msg" "hyperLayout2.hyp[3].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_PNT.msg" "hyperLayout2.hyp[4].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SJNT.msg" "hyperLayout2.hyp[5].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_PNT.msg" "hyperLayout2.hyp[6].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SJNT.msg" "hyperLayout2.hyp[7].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_PNT.msg" "hyperLayout2.hyp[8].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SJNT.msg" "hyperLayout2.hyp[9].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_PNT.msg" "hyperLayout2.hyp[10].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SJNT.msg" "hyperLayout2.hyp[11].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_PNT.msg" "hyperLayout2.hyp[12].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinterBlueprinter_GRP.msg" "hyperLayout2.hyp[13].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0Sctl_GRP.msg" "hyperLayout2.hyp[14].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SCTL.msg" "hyperLayout2.hyp[15].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SCTLShape.msg" "hyperLayout2.hyp[16].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1Sctl_GRP.msg" "hyperLayout2.hyp[17].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SCTL.msg" "hyperLayout2.hyp[18].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SCTLShape.msg" "hyperLayout2.hyp[19].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2Sctl_GRP.msg" "hyperLayout2.hyp[20].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SCTL.msg" "hyperLayout2.hyp[21].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SCTLShape.msg" "hyperLayout2.hyp[22].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3Sctl_GRP.msg" "hyperLayout2.hyp[23].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SCTL.msg" "hyperLayout2.hyp[24].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SCTLShape.msg" "hyperLayout2.hyp[25].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4Sctl_GRP.msg" "hyperLayout2.hyp[26].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SCTL.msg" "hyperLayout2.hyp[27].dn"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SCTLShape.msg" "hyperLayout2.hyp[28].dn"
		;
connectAttr "polySphere3.msg" "hyperLayout2.hyp[29].dn";
connectAttr "polySphere4.msg" "hyperLayout2.hyp[30].dn";
connectAttr "polySphere2.msg" "hyperLayout2.hyp[31].dn";
connectAttr "polySphere1.msg" "hyperLayout2.hyp[32].dn";
connectAttr "polySphere5.msg" "hyperLayout2.hyp[33].dn";
connectAttr "NWSpineJointsRig_GRP.msg" "hyperLayout2.hyp[34].dn";
connectAttr "NWSpineJointsJoint_GRP.msg" "hyperLayout2.hyp[35].dn";
connectAttr "NWSpineJoints1_JNT.msg" "hyperLayout2.hyp[36].dn";
connectAttr "NWSpineJoints2_JNT.msg" "hyperLayout2.hyp[37].dn";
connectAttr "NWSpineJoints3_JNT.msg" "hyperLayout2.hyp[38].dn";
connectAttr "NWSpineJoints4_JNT.msg" "hyperLayout2.hyp[39].dn";
connectAttr "NWSpineJoints5_JNT.msg" "hyperLayout2.hyp[40].dn";
connectAttr "effector1.msg" "hyperLayout2.hyp[41].dn";
connectAttr "NWSpineJointsIK_CRV.msg" "hyperLayout2.hyp[42].dn";
connectAttr "NWSpineJointsIK_CRVShape.msg" "hyperLayout2.hyp[43].dn";
connectAttr "NWSpineJointsIK_CRVShapeOrig.msg" "hyperLayout2.hyp[44].dn";
connectAttr "NWSpineJointsSetup_GRP.msg" "hyperLayout2.hyp[45].dn";
connectAttr "NWSpineJoints_IKH.msg" "hyperLayout2.hyp[46].dn";
connectAttr "NWSpineJointsControl_GRP.msg" "hyperLayout2.hyp[47].dn";
connectAttr "NWSpineJointsIKCluster0Ctl_GRP.msg" "hyperLayout2.hyp[48].dn";
connectAttr "NWSpineJointsIKCluster0_CTL.msg" "hyperLayout2.hyp[49].dn";
connectAttr "NWSpineJointsIKCluster0_CTLShape.msg" "hyperLayout2.hyp[50].dn";
connectAttr "NWSpineJointsIKCluster0_GRP.msg" "hyperLayout2.hyp[51].dn";
connectAttr "NWSpineJointsIKCluster0_CLSHandle.msg" "hyperLayout2.hyp[52].dn";
connectAttr "NWSpineJointsIKCluster0_CLSHandleShape.msg" "hyperLayout2.hyp[53].dn"
		;
connectAttr "NWSpineJointsIKCluster1Ctl_GRP.msg" "hyperLayout2.hyp[54].dn";
connectAttr "NWSpineJointsIKCluster1_CTL.msg" "hyperLayout2.hyp[55].dn";
connectAttr "NWSpineJointsIKCluster1_CTLShape.msg" "hyperLayout2.hyp[56].dn";
connectAttr "NWSpineJointsIKCluster1_GRP.msg" "hyperLayout2.hyp[57].dn";
connectAttr "NWSpineJointsIKCluster1_CLSHandle.msg" "hyperLayout2.hyp[58].dn";
connectAttr "NWSpineJointsIKCluster1_CLSHandleShape.msg" "hyperLayout2.hyp[59].dn"
		;
connectAttr "NWSpineJointsIKCluster2Ctl_GRP.msg" "hyperLayout2.hyp[60].dn";
connectAttr "NWSpineJointsIKCluster2_CTL.msg" "hyperLayout2.hyp[61].dn";
connectAttr "NWSpineJointsIKCluster2_CTLShape.msg" "hyperLayout2.hyp[62].dn";
connectAttr "NWSpineJointsIKCluster2_GRP.msg" "hyperLayout2.hyp[63].dn";
connectAttr "NWSpineJointsIKCluster2_CLSHandle.msg" "hyperLayout2.hyp[64].dn";
connectAttr "NWSpineJointsIKCluster2_CLSHandleShape.msg" "hyperLayout2.hyp[65].dn"
		;
connectAttr "NWSpineJointsIKCluster3Ctl_GRP.msg" "hyperLayout2.hyp[66].dn";
connectAttr "NWSpineJointsIKCluster3_CTL.msg" "hyperLayout2.hyp[67].dn";
connectAttr "NWSpineJointsIKCluster3_CTLShape.msg" "hyperLayout2.hyp[68].dn";
connectAttr "NWSpineJointsIKCluster3_GRP.msg" "hyperLayout2.hyp[69].dn";
connectAttr "NWSpineJointsIKCluster3_CLSHandle.msg" "hyperLayout2.hyp[70].dn";
connectAttr "NWSpineJointsIKCluster3_CLSHandleShape.msg" "hyperLayout2.hyp[71].dn"
		;
connectAttr "makeNurbCircle1.msg" "hyperLayout2.hyp[72].dn";
connectAttr "makeNurbCircle4.msg" "hyperLayout2.hyp[73].dn";
connectAttr "makeNurbCircle3.msg" "hyperLayout2.hyp[74].dn";
connectAttr "makeNurbCircle2.msg" "hyperLayout2.hyp[75].dn";
connectAttr "NWSpineJointsIKCluster3_CLSSet.msg" "hyperLayout2.hyp[76].dn";
connectAttr "NWSpineJointsIKCluster1_CLSSet.msg" "hyperLayout2.hyp[77].dn";
connectAttr "tweakSet1.msg" "hyperLayout2.hyp[78].dn";
connectAttr "NWSpineJointsIKCluster2_CLSSet.msg" "hyperLayout2.hyp[79].dn";
connectAttr "NWSpineJointsIKCluster3_CLSGroupId.msg" "hyperLayout2.hyp[80].dn";
connectAttr "NWSpineJointsIKCluster0_CLSGroupId.msg" "hyperLayout2.hyp[81].dn";
connectAttr "NWSpineJointsIKCluster2_CLSGroupId.msg" "hyperLayout2.hyp[82].dn";
connectAttr "NWSpineJointsIKCluster1_CLSGroupId.msg" "hyperLayout2.hyp[83].dn";
connectAttr "groupId2.msg" "hyperLayout2.hyp[84].dn";
connectAttr "tweak1.msg" "hyperLayout2.hyp[85].dn";
connectAttr "ikSplineSolver.msg" "hyperLayout2.hyp[86].dn";
connectAttr "NWSpineJointsIKCluster0_CLSSet.msg" "hyperLayout2.hyp[87].dn";
connectAttr "NWSpineJointsIKCluster0_CLS.msg" "hyperLayout2.hyp[88].dn";
connectAttr "NWSpineJointsIKCluster0_CLSGroupParts.msg" "hyperLayout2.hyp[89].dn"
		;
connectAttr "groupParts2.msg" "hyperLayout2.hyp[90].dn";
connectAttr "NWSpineJointsIKCluster1_CLS.msg" "hyperLayout2.hyp[91].dn";
connectAttr "NWSpineJointsIKCluster1_CLSGroupParts.msg" "hyperLayout2.hyp[92].dn"
		;
connectAttr "NWSpineJointsIKCluster2_CLS.msg" "hyperLayout2.hyp[93].dn";
connectAttr "NWSpineJointsIKCluster2_CLSGroupParts.msg" "hyperLayout2.hyp[94].dn"
		;
connectAttr "NWSpineJointsIKCluster3_CLS.msg" "hyperLayout2.hyp[95].dn";
connectAttr "NWSpineJointsIKCluster3_CLSGroupParts.msg" "hyperLayout2.hyp[96].dn"
		;
connectAttr "hyperLayout3.msg" "NWHingeJoints_CNT.hl";
connectAttr "NWHingeJointsRoot_GRP.msg" "hyperLayout3.hyp[0].dn";
connectAttr "NWHingeJointsBlueprint_GRP.msg" "hyperLayout3.hyp[1].dn";
connectAttr "NWHingeJointsBlueprintJoint_GRP.msg" "hyperLayout3.hyp[2].dn";
connectAttr "NWHingeJointsBaseBlueprinter_SJNT.msg" "hyperLayout3.hyp[3].dn";
connectAttr "NWHingeJointsBaseBlueprinter_PNT.msg" "hyperLayout3.hyp[4].dn";
connectAttr "NWHingeJointsMiddleBlueprinter_SJNT.msg" "hyperLayout3.hyp[5].dn";
connectAttr "NWHingeJointsMiddleBlueprinter_PNT.msg" "hyperLayout3.hyp[6].dn";
connectAttr "NWHingeJointsEndBlueprinter_SJNT.msg" "hyperLayout3.hyp[7].dn";
connectAttr "NWHingeJointsEndBlueprinter_PNT.msg" "hyperLayout3.hyp[8].dn";
connectAttr "NWHingeJointsBaseBlueprinterSctl_GRP.msg" "hyperLayout3.hyp[9].dn";
connectAttr "NWHingeJointsBaseBlueprinter_SCTL.msg" "hyperLayout3.hyp[10].dn";
connectAttr "NWHingeJointsBaseBlueprinter_SCTLShape.msg" "hyperLayout3.hyp[11].dn"
		;
connectAttr "NWHingeJointsEndBlueprinterSctl_GRP.msg" "hyperLayout3.hyp[12].dn";
connectAttr "NWHingeJointsEndBlueprinter_SCTL.msg" "hyperLayout3.hyp[13].dn";
connectAttr "NWHingeJointsEndBlueprinter_SCTLShape.msg" "hyperLayout3.hyp[14].dn"
		;
connectAttr "NWHingeJointsaxisCtl_GRP.msg" "hyperLayout3.hyp[15].dn";
connectAttr "NWHingeJointsaxisCtlCtl_GRP.msg" "hyperLayout3.hyp[16].dn";
connectAttr "NWHingeJointsaxisCtlXCtl_GRP.msg" "hyperLayout3.hyp[17].dn";
connectAttr "NWHingeJointsaxisCtlX_CTL.msg" "hyperLayout3.hyp[18].dn";
connectAttr "curveShape2.msg" "hyperLayout3.hyp[19].dn";
connectAttr "NWHingeJointsaxisCtlYCtl_GRP.msg" "hyperLayout3.hyp[20].dn";
connectAttr "NWHingeJointsaxisCtlY_CTL.msg" "hyperLayout3.hyp[21].dn";
connectAttr "curveShape3.msg" "hyperLayout3.hyp[22].dn";
connectAttr "NWHingeJointsaxisCtlZCtl_GRP.msg" "hyperLayout3.hyp[23].dn";
connectAttr "NWHingeJointsaxisCtlZ_CTL.msg" "hyperLayout3.hyp[24].dn";
connectAttr "curveShape4.msg" "hyperLayout3.hyp[25].dn";
connectAttr "NWHingeJointsMiddleBlueprinterSctl_GRP.msg" "hyperLayout3.hyp[26].dn"
		;
connectAttr "NWHingeJointsMiddleBlueprinter_SCTL.msg" "hyperLayout3.hyp[27].dn";
connectAttr "NWHingeJointsMiddleBlueprinter_SCTLShape.msg" "hyperLayout3.hyp[28].dn"
		;
connectAttr "NWHingeJointsBaseEndConst_PNT.msg" "hyperLayout3.hyp[29].dn";
connectAttr "NWHingeJointsBaseEndConst_AIM.msg" "hyperLayout3.hyp[30].dn";
connectAttr "NWHingeJointsDirectionSctl_GRP.msg" "hyperLayout3.hyp[31].dn";
connectAttr "NWHingeJointsDirection_SCTL.msg" "hyperLayout3.hyp[32].dn";
connectAttr "curveShape1.msg" "hyperLayout3.hyp[33].dn";
connectAttr "NWHingeJointsDirection_SJNT.msg" "hyperLayout3.hyp[34].dn";
connectAttr "NWHingeJointsDirection_PNT.msg" "hyperLayout3.hyp[35].dn";
connectAttr "NWHingeJointsArrowConst_PNT.msg" "hyperLayout3.hyp[36].dn";
connectAttr "NWHingeJointsArrowConst_AIM.msg" "hyperLayout3.hyp[37].dn";
connectAttr "NWHingeJointsaxisCtlZ_PMA.msg" "hyperLayout3.hyp[38].dn";
connectAttr "polyCube1.msg" "hyperLayout3.hyp[39].dn";
connectAttr "polySphere6.msg" "hyperLayout3.hyp[40].dn";
connectAttr "polySphere7.msg" "hyperLayout3.hyp[41].dn";
connectAttr "NWHingeJointsaxisCtlY_PMA.msg" "hyperLayout3.hyp[42].dn";
connectAttr "NWHingeJointsaxisCtlX_PMA.msg" "hyperLayout3.hyp[43].dn";
connectAttr "NWHingeJointsRig_GRP.msg" "hyperLayout3.hyp[44].dn";
connectAttr "NWHingeJointsJoint_GRP.msg" "hyperLayout3.hyp[45].dn";
connectAttr "NWHingeJoints1_JNT.msg" "hyperLayout3.hyp[46].dn";
connectAttr "NWHingeJoints2_JNT.msg" "hyperLayout3.hyp[47].dn";
connectAttr "NWHingeJoints3_JNT.msg" "hyperLayout3.hyp[48].dn";
connectAttr "effector2.msg" "hyperLayout3.hyp[49].dn";
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsJoint_GRP|NWHingeJoints1_JNT|NWHingeJointsPole_PCT.msg" "hyperLayout3.hyp[50].dn"
		;
connectAttr "NWHingeJointsSetup_GRP.msg" "hyperLayout3.hyp[51].dn";
connectAttr "NWHingeJoints_IKH.msg" "hyperLayout3.hyp[52].dn";
connectAttr "NWHingeJointsPole_PVC.msg" "hyperLayout3.hyp[53].dn";
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJoints_IKH|NWHingeJointsIK_PCT.msg" "hyperLayout3.hyp[54].dn"
		;
connectAttr "NWHingeJointsPole_GRP.msg" "hyperLayout3.hyp[55].dn";
connectAttr "NWHingeJointsPole_LOC.msg" "hyperLayout3.hyp[56].dn";
connectAttr "NWHingeJointsPole_LOCShape.msg" "hyperLayout3.hyp[57].dn";
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsSetup_GRP|NWHingeJointsPole_GRP|NWHingeJointsPole_PCT.msg" "hyperLayout3.hyp[58].dn"
		;
connectAttr "NWHingeJointsControl_GRP.msg" "hyperLayout3.hyp[59].dn";
connectAttr "NWHingeJointsBaseCtl_GRP.msg" "hyperLayout3.hyp[60].dn";
connectAttr "NWHingeJointsBase_CTL.msg" "hyperLayout3.hyp[61].dn";
connectAttr "NWHingeJointsBase_CTLShape.msg" "hyperLayout3.hyp[62].dn";
connectAttr "NWHingeJointsIKCtl_GRP.msg" "hyperLayout3.hyp[63].dn";
connectAttr "NWHingeJointsIK_CTL.msg" "hyperLayout3.hyp[64].dn";
connectAttr "NWHingeJointsIK_CTLShape.msg" "hyperLayout3.hyp[65].dn";
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsIKCtl_GRP|NWHingeJointsIK_PCT.msg" "hyperLayout3.hyp[66].dn"
		;
connectAttr "NWHingeJointsPoleCtl_GRP.msg" "hyperLayout3.hyp[67].dn";
connectAttr "NWHingeJointsPole_CTL.msg" "hyperLayout3.hyp[68].dn";
connectAttr "NWHingeJointsPole_CTLShape.msg" "hyperLayout3.hyp[69].dn";
connectAttr "|nwRigRoot_GRP|modules_GRP|NWHingeJointsRoot_GRP|NWHingeJointsRig_GRP|NWHingeJointsControl_GRP|NWHingeJointsPoleCtl_GRP|NWHingeJointsIK_PCT.msg" "hyperLayout3.hyp[70].dn"
		;
connectAttr "ikRPsolver.msg" "hyperLayout3.hyp[71].dn";
connectAttr "makeNurbCircle5.msg" "hyperLayout3.hyp[72].dn";
connectAttr "NWHingeJointsaxisCtlX_CTL.tx" "NWHingeJointsaxisCtlX_PMA.i1";
connectAttr "NWHingeJointsaxisCtlY_CTL.ty" "NWHingeJointsaxisCtlY_PMA.i1";
connectAttr "NWHingeJointsaxisCtlZ_CTL.tz" "NWHingeJointsaxisCtlZ_PMA.i1";
connectAttr "NWSpineJointsIKCluster0_CLSGroupParts.og" "NWSpineJointsIKCluster0_CLS.ip[0].ig"
		;
connectAttr "NWSpineJointsIKCluster0_CLSGroupId.id" "NWSpineJointsIKCluster0_CLS.ip[0].gi"
		;
connectAttr "NWSpineJointsIKCluster0_CLSHandle.wm" "NWSpineJointsIKCluster0_CLS.ma"
		;
connectAttr "NWSpineJointsIKCluster0_CLSHandleShape.x" "NWSpineJointsIKCluster0_CLS.x"
		;
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "NWSpineJointsIKCluster0_CLSGroupId.msg" "NWSpineJointsIKCluster0_CLSSet.gn"
		 -na;
connectAttr "NWSpineJointsIK_CRVShape.iog.og[0]" "NWSpineJointsIKCluster0_CLSSet.dsm"
		 -na;
connectAttr "NWSpineJointsIKCluster0_CLS.msg" "NWSpineJointsIKCluster0_CLSSet.ub[0]"
		;
connectAttr "tweak1.og[0]" "NWSpineJointsIKCluster0_CLSGroupParts.ig";
connectAttr "NWSpineJointsIKCluster0_CLSGroupId.id" "NWSpineJointsIKCluster0_CLSGroupParts.gi"
		;
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "NWSpineJointsIK_CRVShape.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "NWSpineJointsIK_CRVShapeOrig.ws" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "NWSpineJointsIKCluster1_CLSGroupParts.og" "NWSpineJointsIKCluster1_CLS.ip[0].ig"
		;
connectAttr "NWSpineJointsIKCluster1_CLSGroupId.id" "NWSpineJointsIKCluster1_CLS.ip[0].gi"
		;
connectAttr "NWSpineJointsIKCluster1_CLSHandle.wm" "NWSpineJointsIKCluster1_CLS.ma"
		;
connectAttr "NWSpineJointsIKCluster1_CLSHandleShape.x" "NWSpineJointsIKCluster1_CLS.x"
		;
connectAttr "NWSpineJointsIKCluster1_CLSGroupId.msg" "NWSpineJointsIKCluster1_CLSSet.gn"
		 -na;
connectAttr "NWSpineJointsIK_CRVShape.iog.og[2]" "NWSpineJointsIKCluster1_CLSSet.dsm"
		 -na;
connectAttr "NWSpineJointsIKCluster1_CLS.msg" "NWSpineJointsIKCluster1_CLSSet.ub[0]"
		;
connectAttr "NWSpineJointsIKCluster0_CLS.og[0]" "NWSpineJointsIKCluster1_CLSGroupParts.ig"
		;
connectAttr "NWSpineJointsIKCluster1_CLSGroupId.id" "NWSpineJointsIKCluster1_CLSGroupParts.gi"
		;
connectAttr "NWSpineJointsIKCluster2_CLSGroupParts.og" "NWSpineJointsIKCluster2_CLS.ip[0].ig"
		;
connectAttr "NWSpineJointsIKCluster2_CLSGroupId.id" "NWSpineJointsIKCluster2_CLS.ip[0].gi"
		;
connectAttr "NWSpineJointsIKCluster2_CLSHandle.wm" "NWSpineJointsIKCluster2_CLS.ma"
		;
connectAttr "NWSpineJointsIKCluster2_CLSHandleShape.x" "NWSpineJointsIKCluster2_CLS.x"
		;
connectAttr "NWSpineJointsIKCluster2_CLSGroupId.msg" "NWSpineJointsIKCluster2_CLSSet.gn"
		 -na;
connectAttr "NWSpineJointsIK_CRVShape.iog.og[3]" "NWSpineJointsIKCluster2_CLSSet.dsm"
		 -na;
connectAttr "NWSpineJointsIKCluster2_CLS.msg" "NWSpineJointsIKCluster2_CLSSet.ub[0]"
		;
connectAttr "NWSpineJointsIKCluster1_CLS.og[0]" "NWSpineJointsIKCluster2_CLSGroupParts.ig"
		;
connectAttr "NWSpineJointsIKCluster2_CLSGroupId.id" "NWSpineJointsIKCluster2_CLSGroupParts.gi"
		;
connectAttr "NWSpineJointsIKCluster3_CLSGroupParts.og" "NWSpineJointsIKCluster3_CLS.ip[0].ig"
		;
connectAttr "NWSpineJointsIKCluster3_CLSGroupId.id" "NWSpineJointsIKCluster3_CLS.ip[0].gi"
		;
connectAttr "NWSpineJointsIKCluster3_CLSHandle.wm" "NWSpineJointsIKCluster3_CLS.ma"
		;
connectAttr "NWSpineJointsIKCluster3_CLSHandleShape.x" "NWSpineJointsIKCluster3_CLS.x"
		;
connectAttr "NWSpineJointsIKCluster3_CLSGroupId.msg" "NWSpineJointsIKCluster3_CLSSet.gn"
		 -na;
connectAttr "NWSpineJointsIK_CRVShape.iog.og[4]" "NWSpineJointsIKCluster3_CLSSet.dsm"
		 -na;
connectAttr "NWSpineJointsIKCluster3_CLS.msg" "NWSpineJointsIKCluster3_CLSSet.ub[0]"
		;
connectAttr "NWSpineJointsIKCluster2_CLS.og[0]" "NWSpineJointsIKCluster3_CLSGroupParts.ig"
		;
connectAttr "NWSpineJointsIKCluster3_CLSGroupId.id" "NWSpineJointsIKCluster3_CLSGroupParts.gi"
		;
connectAttr "NWSpineJointsSpineChainBlueprinter0_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "NWSpineJointsSpineChainBlueprinter1_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "NWSpineJointsSpineChainBlueprinter2_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "NWSpineJointsSpineChainBlueprinter3_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "NWSpineJointsSpineChainBlueprinter4_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "NWHingeJointsBaseBlueprinter_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "NWHingeJointsMiddleBlueprinter_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "NWHingeJointsEndBlueprinter_SCTLShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
connectAttr "ikSplineSolver.msg" ":ikSystem.sol" -na;
// End of nwRig.ma
