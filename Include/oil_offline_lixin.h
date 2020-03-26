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

#define ANA_SMFLUX
#define ANA_STFLUX
#define ANA_SSFLUX
#define ANA_BTFLUX
#define ANA_BSFLUX

/*
 *  *  * **-----------------------------------------------------------------------------
 *   *   * **  Offline settings
 *    *    * **-----------------------------------------------------------------------------
 *     *     * */
#define OFFLINE
#undef OCLIMATOLOGY
#undef AKTCLIMATOLOGY
#define ANA_NUDGCOEF


/*
 *  * **-----------------------------------------------------------------------------
 *   * **  Adding offline passive tracers
 *    * **-----------------------------------------------------------------------------
 *     * */
#define OFFLINE_TPASSIVE
#ifdef OFFLINE_TPASSIVE
# define T_PASSIVE
# define ANA_BPFLUX
# define ANA_SPFLUX
#endif

/*
 *  *  * **-----------------------------------------------------------------------------
 *   *   * **  Adding offline floats
 *    *    * **-----------------------------------------------------------------------------
 *     *     * */
#define OFFLINE_FLOATS
#ifdef OFFLINE_FLOATS
# define FLOATS
# define FLOAT_OIL
# undef FLOAT_VWALK
# undef WOIL_INTEGRATED
# undef OIL_DEBUG
# undef OIL_EULR
#endif