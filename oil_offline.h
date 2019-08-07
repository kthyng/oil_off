/*
 * ** svn $Id: ias.h 830 2017-01-24 21:21:11Z arango $
 * *******************************************************************************
 * ** Copyright (c) 2002-2018 The ROMS/TOMS Group                               **
 * **   Licensed under a MIT/X style license                                    **
 * **   See License_ROMS.txt                                                    **
 * *******************************************************************************
 * **
 * ** Options for NGOM 1/25 DEG resolution.
 * **
 * ** Application flag:   NGOM_04_offline
 * ** Input script:       ocean_NGOM_04_offline.in
 * */

#define ROMS_MODEL
#define NLM_DRIVER              /* Nonlinear Basic State trajectory */

#define UV_QDRAG
#define UV_VIS2
#define MIX_S_UV               /*mixing of momentum along constant s surfaces*/
#define SPLINES_VDIFF
#define SPLINES_VVISC
#define SOLVE3D
#define CURVGRID
#define MASKING

#define  GLS_MIXING
#ifdef GLS_MIXING
# define KANTHA_CLAYSON
# define N2S2_HORAVG
# define RI_SPLINES
#endif

#undef FORWARD_WRITE
#undef FLOATS
#undef FLOAT_VWALK

#define OFFLINE
#define OCLIMATOLOGY
#undef AKTCLIMATOLOGY
#undef T_PASSIVE

#define BIOLOGY
#define OFFLINE_BIOLOGY
#define BIO_FENNEL

#ifdef BIO_FENNEL
# define ANA_BIOLOGY
# undef DIURNAL_SRFLUX
# define CARBON
# define DENITRIFICATION
# define OXYGEN
# define BIO_SEDIMENT
# undef DIAGNOSTICS_BIO
# define ANA_BPFLUX
# define ANA_SPFLUX
#endif

#undef ANA_SRFLUX

#define USE_DEBUG
#define ANA_NUDGCOEF
#define ANA_INITIAL
