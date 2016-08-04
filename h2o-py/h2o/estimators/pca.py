#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from .estimator_base import H2OEstimator


class H2OPrincipalComponentAnalysisEstimator(H2OEstimator):
    """
    Principal Components Analysis


    Parameters
    ----------
      model_id : str
        Destination id for this model; auto-generated if not specified.

      training_frame : str
        Id of the training data frame (Not required, to allow initial validation of model parameters).

      validation_frame : str
        Id of the validation data frame.

      ignored_columns : list(str)
        Names of columns to ignore for training.

      ignore_const_cols : bool
        Ignore constant columns.
        Default: True

      score_each_iteration : bool
        Whether to score during each iteration of model training.
        Default: False

      transform : "NONE" | "STANDARDIZE" | "NORMALIZE" | "DEMEAN" | "DESCALE"
        Transformation of training data
        Default: "NONE"

      pca_method : "GramSVD" | "Power" | "Randomized" | "GLRM"
        Method for computing PCA (Caution: Power and GLRM are currently experimental and unstable)
        Default: "GramSVD"

      k : int, required
        Rank of matrix approximation
        Default: 1

      max_iterations : int
        Maximum training iterations
        Default: 1000

      use_all_factor_levels : bool
        Whether first factor level is included in each categorical expansion
        Default: False

      compute_metrics : bool
        Whether to compute metrics on the training data
        Default: True

      impute_missing : bool
        Whether to impute missing entries with the column mean
        Default: False

      seed : int
        RNG seed for initialization
        Default: -1

      max_runtime_secs : float
        Maximum allowed runtime in seconds for model training. Use 0 to disable.
        Default: 0.0

    """
    def __init__(self, **kwargs):
        super(H2OPrincipalComponentAnalysisEstimator, self).__init__()
        self._parms = {}
        for name in ["model_id", "training_frame", "validation_frame", "ignored_columns", "ignore_const_cols",
                     "score_each_iteration", "transform", "pca_method", "k", "max_iterations", "use_all_factor_levels",
                     "compute_metrics", "impute_missing", "seed", "max_runtime_secs"]:
            pname = name[:-1] if name[-1] == '_' else name
            self._parms[pname] = kwargs[name] if name in kwargs else None

    @property
    def training_frame(self):
        return self._parms["training_frame"]

    @training_frame.setter
    def training_frame(self, value):
        self._parms["training_frame"] = value

    @property
    def validation_frame(self):
        return self._parms["validation_frame"]

    @validation_frame.setter
    def validation_frame(self, value):
        self._parms["validation_frame"] = value

    @property
    def ignored_columns(self):
        return self._parms["ignored_columns"]

    @ignored_columns.setter
    def ignored_columns(self, value):
        self._parms["ignored_columns"] = value

    @property
    def ignore_const_cols(self):
        return self._parms["ignore_const_cols"]

    @ignore_const_cols.setter
    def ignore_const_cols(self, value):
        self._parms["ignore_const_cols"] = value

    @property
    def score_each_iteration(self):
        return self._parms["score_each_iteration"]

    @score_each_iteration.setter
    def score_each_iteration(self, value):
        self._parms["score_each_iteration"] = value

    @property
    def transform(self):
        return self._parms["transform"]

    @transform.setter
    def transform(self, value):
        self._parms["transform"] = value

    @property
    def pca_method(self):
        return self._parms["pca_method"]

    @pca_method.setter
    def pca_method(self, value):
        self._parms["pca_method"] = value

    @property
    def k(self):
        return self._parms["k"]

    @k.setter
    def k(self, value):
        self._parms["k"] = value

    @property
    def max_iterations(self):
        return self._parms["max_iterations"]

    @max_iterations.setter
    def max_iterations(self, value):
        self._parms["max_iterations"] = value

    @property
    def use_all_factor_levels(self):
        return self._parms["use_all_factor_levels"]

    @use_all_factor_levels.setter
    def use_all_factor_levels(self, value):
        self._parms["use_all_factor_levels"] = value

    @property
    def compute_metrics(self):
        return self._parms["compute_metrics"]

    @compute_metrics.setter
    def compute_metrics(self, value):
        self._parms["compute_metrics"] = value

    @property
    def impute_missing(self):
        return self._parms["impute_missing"]

    @impute_missing.setter
    def impute_missing(self, value):
        self._parms["impute_missing"] = value

    @property
    def seed(self):
        return self._parms["seed"]

    @seed.setter
    def seed(self, value):
        self._parms["seed"] = value

    @property
    def max_runtime_secs(self):
        return self._parms["max_runtime_secs"]

    @max_runtime_secs.setter
    def max_runtime_secs(self, value):
        self._parms["max_runtime_secs"] = value

