/*
** svn $Id: ias.h 830 2017-01-24 21:21:11Z arango $
*******************************************************************************
** Copyright (c) 2002-2018 The ROMS/TOMS Group                               **
**   Licensed under a MIT/X style license                                    **
**   See License_ROMS.txt                                                    **
*******************************************************************************
**
** Options for NGOM 1/25 DEG resolution.
**
** Application flag:   oil_03
** Input script:       ocean_oil_03.in
*/

#undef WRF_MODEL
#undef SWAN_MODEL
#define ROMS_MODEL

#define DIAGNOSTICS

/* Oil */
#define OUT_DOUBLE

#define FLOATS
#define FLOAT_OIL
#undef FLOAT_VWALK
#undef WOIL_INTEGRATED
#undef OIL_DEBUG

/*
 *  *  *  * **-----------------------------------------------------------------------------
 *   *   *   * **  Offline settings
 *    *    *    * **-----------------------------------------------------------------------------
 *     *     *     * */
#define OFFLINE
#ifdef OFFLINE
#define OCLIMATOLOGY
/*#undef ANA_AKTCLIMA*/

/* For inclusion of mixing variables from history file, 
 *  * you need to either define the following individual mixing variables 
 *   * or define AKXCLIMATOLOGY and/or MIXCLIMATOLOGY
 *    *
 *     * AKTCLIMATOLOGY and AKSCLIMATOLOGY and AKVCLIMATLOGY define AKXCLIMATOLOGY
 *      * TKECLIMATOLOGY and GLSCLIMATOLOGY define MIXCLIMATOLOGY
 *      */

/*
 * #define AKTCLIMATOLOGY
 * #define AKSCLIMATOLOGY
 * #define AKVCLIMATOLOGY
 * #undef TKECLIMATOLOGY
 * #undef GLSCLIMATOLOGY
 * */


#define MIXCLIMATOLOGY
#define AKXCLIMATOLOGY


/*
 *  *  * **-----------------------------------------------------------------------------
 *   *   * **  Adding offline passive tracers
 *    *    * **-----------------------------------------------------------------------------
 *     *     * */
#define OFFLINE_TPASSIVE
#ifdef OFFLINE_TPASSIVE
# define T_PASSIVE
# define ANA_BPFLUX
# define ANA_SPFLUX
#endif

/*
 *  *  *  * **-----------------------------------------------------------------------------
 *   *   *   * **  Adding offline floats
 *    *    *    * **-----------------------------------------------------------------------------
 *     *     *     * */
#define OFFLINE_FLOATS
#ifdef OFFLINE_FLOATS
# define FLOATS
# define FLOAT_OIL
# undef FLOAT_VWALK
# undef WOIL_INTEGRATED
# undef OIL_DEBUG
# undef OIL_EULR
#endif

#endif


/* no mixing */
#define ANA_VMIX
#ifdef ANA_VMIX
#undef GLS_MIXING
#endif

#define ANA_AKTCLIMA
#define ANA_INITIAL
#define ANA_BSFLUX
#define ANA_BTFLUX

#undef  BULK_FLUXES
#ifdef BULK_FLUXES
# undef  QCORRECTION
# undef  LONGWAVE
# define LONGWAVE_OUT
# define SPECIFIC_HUMIDITY
# define SOLAR_SOURCE
# undef CLOUDS
#else
# undef  QCORRECTION
# undef  SOLAR_SOURCE
# undef  DIURNAL_SRFLUX
#define ANA_SMFLUX
#define ANA_STFLUX
#define ANA_SSFLUX
#endif

/*
**-----------------------------------------------------------------------------
**  Nonlinear basic state settings.
**-----------------------------------------------------------------------------
*/
#define  AVERAGES               /*Write out time-averaged data*/
#undef  AVERAGES_FLUXES
#define UV_ADV
#define DJ_GRADPS
#define UV_COR
#define UV_QDRAG
#define UV_VIS2
#define MIX_S_UV               /*mixing of momentum along constant s surfaces*/
#define SPLINES_VDIFF
#define SPLINES_VVISC
#define TS_U3HADVECTION
#define TS_C4VADVECTION
#define SOLVE3D
#define SALINITY
#define NONLIN_EOS
#define CURVGRID
#define MASKING
#undef  SRELAXATION            /*salinity relaxation as freshwater flux*/

/*#undef  GLS_MIXING*/
#ifdef GLS_MIXING
# undef  LMD_MIXING
# define KANTHA_CLAYSON
# define N2S2_HORAVG
# define RI_SPLINES
#endif

/*
 * **-----------------------------------------------------------------------------
 * **  Adding Passive tracers
 * **-----------------------------------------------------------------------------
 * */
#define T_PASSIVE
#define ANA_BPFLUX
#define ANA_SPFLUX
