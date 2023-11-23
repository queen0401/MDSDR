# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:        Forms
# @Author:      GuoSijia
# @Purpose:
# @Created:     2018-09-24
# @update:      2018-09-24 0:35
# @Software:    PyCharm
# -------------------------------------------------------------------------------
# from Base import compute
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField, SelectField, HiddenField
from wtforms.fields import core
from wtforms.validators import Required


class NewForm(FlaskForm):
    name = StringField('Please Enter A Gene ID', validators=[Required()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    name = StringField('', validators=[Required()])
    submit = SubmitField('Submit', id='notice')


class SearchForm2(FlaskForm):
    name = StringField('Gene ID or Symbol', validators=[Required()])
    submit = SubmitField('Submit', id='notice')


class GeneForm(FlaskForm):
    adname = StringField('Gene ID or Symbol', id='sf', validators=[Required()])
    adsubmit = SubmitField('Submit')


class AdvancedForm(FlaskForm):
    # adname = StringField('Chr',id='sf2',validators=[Required()])

    Chr = SelectField("Chr",
                      coerce=int,
                      id='sf',
                      choices=[(1, 'All'),
                               (2, '1'),
                               (3, '2'),
                               (4, '3'),
                               (5, '4'),
                               (6, '5'),
                               (7, '6'),
                               (8, '7'),
                               (9, '8'),
                               (10, '9'),
                               (11, '10'),
                               (12, '11'),
                               (13, '12'),
                               (14, '13'),
                               (15, '14'),
                               (16, '15'),
                               (17, '16'),
                               (18, '17'),
                               (19, '18'),
                               (20, '19'),
                               (21, '20'),
                               (22, '21'),
                               (23, '22'),
                               (24, 'X'),
                               (25, 'Y')])
    start = StringField('Start', id='sf3', validators=[])
    end = StringField('End', id='sf4', validators=[])

    DNV = SelectField("Mutation_Type",
                      coerce=int,
                      id='sf',
                      choices=[(1, 'exonic'),
                               (2, 'splicing'),
                               (3, 'intergenic'),
                               (4, 'intronic'),
                               (5, 'upstream'),
                               (6, 'missense'),
                               (7, "UTR3"),
                               (8, "UTR5")])
    disorder = SelectField("Disorders",
                           coerce=int,
                           id='sf',
                           choices=[(1, 'Psychiatric Disorder - Attention Deficit Hyperactivity Disorder (ADHD)'),
                                    (2, 'Psychiatric Disorder - Autism (ASD)'),
                                    (3, 'Psychiatric Disorder - Bipolar Disorder (BP)'),
                                    (4, 'Psychiatric Disorder - Developmental Delay (DD)'),
                                    (5, 'Psychiatric Disorder - Intellectual Disability(ID)'),
                                    (6, 'Psychiatric Disorder - Mix (Autism or Schizophrenia)'),
                                    (7, 'Psychiatric Disorder - Obsessive-Compulsive Disorder (OCD)'),
                                    (8, 'Psychiatric Disorder - Schizophrenia (SCZ)'),
                                    (9, 'Psychiatric Disorder - Sotos-like syndrome'),
                                    (10, 'Psychiatric Disorder - Tourette Disorder (TD)'),
                                    (11, 'Neurological Disorde - Amyotrophic Lateral Sclerosis (ALS)'),
                                    (12, 'Neurological Disorder - Cerebral Palsy (CP)'),
                                    (13, 'Neurological Disorder - Developmental and Epileptic Encephalopathies (DEE)'),
                                    (14, 'Neurological Disorder - Early-onset Alzheimer Disorder (eoAD)'),
                                    (15, 'Neurological Disorder - Early-onset High Myopia (eoHM)'),
                                    (16, 'Neurological Disorder - Early-onset Parkinson Disorder (eoPD)'),
                                    (17, 'Neurological Disorder - Epileptic Encephalopathies (EE)'),
                                    (18, 'Neurological Disorder - Infantile Spasms (IS)'),
                                    (19, 'Neurological Disorder - Lennox Gastaut Syndrome (LGS)'),
                                    (20,
                                     'Neurological Disorder - Mesial Temporal Lobe Epilepsy with Hippocampal Sclerosis (MTLE-HS)'),
                                    (21, 'Neurological Disorder - Neural Tube Defects (NTD)'),
                                    (22, 'Neurological Disorder - Sporadic Infantile Spasm Syndrome (IS)'),
                                    (23, 'Birth Defect - Acromelic Frontonasal Dysostosis (AFND)'),
                                    (24, 'Birth Defect - Anophthalmia and Microphthalmia (A/M)'),
                                    (25, 'Birth Defect - Cantu Syndrome (CS)'),
                                    (26, 'Birth Defect - Congenital Diaphragmatic Hernia (CDH)'),
                                    (27, 'Birth Defect - Congenital Heart Disease (CHD)'),
                                    (28, 'Control Study - Fetal non-Preterm birth (non-PTB)'),
                                    (29, 'Control Study - Fetal preterm birth (PTB)'),
                                    (30, 'Control Study - Sibling Control'),
                                    (31, 'Control Study - Uncharacterized (Mixed healthy control)')])

    submit2 = SubmitField('Submit')


class AdvancedForm2(FlaskForm):
    # Using CNV Form
    # adname = StringField('Chr',id='sf2',validators=[Required()])

    Chr2 = SelectField("Chr",
                       coerce=int,
                       id='sf',
                       choices=[(1, 'All'),
                                (2, '1'),
                                (3, '2'),
                                (4, '3'),
                                (5, '4'),
                                (6, '5'),
                                (7, '6'),
                                (8, '7'),
                                (9, '8'),
                                (10, '9'),
                                (11, '10'),
                                (12, '11'),
                                (13, '12'),
                                (14, '13'),
                                (15, '14'),
                                (16, '15'),
                                (17, '16'),
                                (18, '17'),
                                (19, '18'),
                                (20, '19'),
                                (21, '20'),
                                (22, '21'),
                                (23, '22'),
                                (24, 'X'),
                                (25, 'Y')])
    start2 = StringField('Start', id='sf3', validators=[])
    end2 = StringField('End', id='sf4', validators=[])

    CNV = SelectField("Mutation_Type",
                      coerce=int,
                      id='sf',
                      choices=[(1, 'Del'),
                               (2, 'Dup')])
    disorder2 = SelectField("Disorders",
                            coerce=int,
                            id='sf',
                            choices=[(1, 'Attention Deficit Hyperactivity Disorder'),
                                     (2, 'Autism'),
                                     (3, 'Bipolar Disorder'),
                                     (4, 'Control'),
                                     (5, 'Intellectual Disability'),
                                     (6, 'Obsessive-Compulsive Disorder'),
                                     (7, 'Schizophrenia'),
                                     (8, 'Tourette Disorder')])

    submit3 = SubmitField('Submit')


class MutationsMrnaForm(FlaskForm):
    mrna_radio = core.RadioField(
        label="mRNA – level impact",
        choices=(
            ("m1", 'all mRNA isoforms'),
            ("m2",
             'mRNA isoforms with coding regions being impact <span data-toggle="tooltip" data-placement="top" title="The mRNA isoforms of the selected mutation falls on the exon"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></span>'),
            ("m3",
             'brain expressed mRNA isoforms  <span data-toggle="tooltip" data-placement="top" title="Have one expressed value of startswith brain tissue(log2(TPM+1) >= 1)"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></span>'),
            ("m4",
             'mRNA isoforms with coding regions being impact and brain expressed mRNA isoforms  <span data-toggle="tooltip" data-placement="top" title="The mRNA isoforms of the selected mutation falls on the exon and have one expressed value of startswith brain tissue(log2(TPM+1) >= 1"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></span>')
        ),
        default="m1"
        # coerce=int  #限制是int类型的
    )
    mrna_submit = SubmitField('Show')


class MutationProteinForm(FlaskForm):
    protein_radio = core.RadioField(
        label="Protein – level impact",
        choices=(
            ("p1", 'all proteins'),
            ("p2",
             'Impacted proteins  <span data-toggle="tooltip" data-placement="top" title="The transcript of the selected mutation falls on the exon"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></span>'),
            ("p3",
             'brain expressed proteins <span data-toggle="tooltip" data-placement="top" title="The expressed value of brain (Median protein expression, log <sub>10</sub> normalized iBAQ intensity) >=0.5 )"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></span>'),
            ("p4",
             'Impacted proteins and brain expressed proteins <span data-toggle="tooltip" data-placement="top" title="The transcript of the selected mutation falls on the exon and expressed value of brain (Median protein expression, lg normalized iBAQ intensit) >=0.5 )"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></span>'),
        ),
        default="p1"
        # coerce=int  #限制是int类型的
    )
    protein_submit = SubmitField('Show')
