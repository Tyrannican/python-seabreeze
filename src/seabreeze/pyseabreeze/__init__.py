"""This is a wrapper for the pyusb-implementation of the seabreeze-library

"""
from seabreeze.pyseabreeze.api import SeaBreezeAPI
from seabreeze.pyseabreeze.exceptions import (SeaBreezeError,
                                              SeaBreezeNumFeaturesError)
from seabreeze.pyseabreeze.devices import SeaBreezeDevice

"""
from seabreeze.pyseabreeze.features import (SeaBreezeFeature,
                                            SeaBreezeRawUSBBusAccessFeature,
                                            SeaBreezeSpectrometerFeature,
                                            SeaBreezePixelBinningFeature,
                                            SeaBreezeThermoElectricFeature,
                                            SeaBreezeIrradCalFeature,
                                            SeaBreezeEthernetConfigurationFeature,
                                            SeaBreezeMulticastFeature,
                                            SeaBreezeIPv4Feature,
                                            SeaBreezeDHCPServerFeature,
                                            SeaBreezeNetworkConfigurationFeature,
                                            SeaBreezeWifiConfigurationFeature,
                                            SeaBreezeGPIOFeature,
                                            SeaBreezeEEPROMFeature,
                                            SeaBreezeLightSourceFeature,
                                            SeaBreezeStrobeLampFeature,
                                            SeaBreezeContinuousStrobeFeature,
                                            SeaBreezeShutterFeature,
                                            SeaBreezeNonlinearityCoefficientsFeature,
                                            SeaBreezeTemperatureFeature,
                                            SeaBreezeIntrospectionFeature,
                                            SeaBreezeSpectrumProcessingFeature,
                                            SeaBreezeRevisionFeature,
                                            SeaBreezeOpticalBenchFeature,
                                            SeaBreezeStrayLightCoefficientsFeature,
                                            SeaBreezeDataBufferFeature,
                                            SeaBreezeFastBufferFeature,
                                            SeaBreezeAcquisitionDelayFeature,
                                            SeaBreezeI2CMasterFeature)
"""
