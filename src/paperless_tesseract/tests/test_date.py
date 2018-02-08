import os
from unittest import skipIf, mock

import pyocr
from django.test import TestCase

from ..parsers import RasterisedDocumentParser
import datetime
from dateutil import tz


class TestDate(TestCase):
    SAMPLE_FILES = os.path.join(os.path.dirname(__file__), "samples")

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_1_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_1.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 4, 1, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_1_png(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_1.png")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), False)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 4, 1, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_2_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_2.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2013, 2, 1, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_2_png(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_2.png")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), False)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2013, 2, 1, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_3_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_3.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 10, 5, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_3_png(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_3.png")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), False)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 10, 5, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_4_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_4.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 10, 5, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_4_png(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_4.png")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), False)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 10, 5, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_5_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_5.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 12, 17, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_5_png(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_5.png")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), False)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 12, 17, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_6_pdf_us(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_6.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        document.DATE_ORDER = "MDY"
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 12, 17, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_6_png_us(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_6.png")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        document.DATE_ORDER = "MDY"
        self.assertEqual(document._is_ocred(), False)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 12, 17, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_6_pdf_eu(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_6.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(), None)

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_6_png_eu(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_6.png")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), False)
        self.assertEqual(document.get_date(), None)

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_7_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_7.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2018, 4, 1, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_8_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_8.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2017, 12, 31, 0, 0,
                                           tzinfo=tz.tzutc()))

    @mock.patch(
        "paperless_tesseract.parsers.RasterisedDocumentParser.SCRATCH",
        SAMPLE_FILES
    )
    def test_get_text_9_pdf(self):
        input_file = os.path.join(self.SAMPLE_FILES, "tests_date_9.pdf")
        document = RasterisedDocumentParser(input_file)
        document.get_text()
        self.assertEqual(document._is_ocred(), True)
        self.assertEqual(document.get_date(),
                         datetime.datetime(2017, 12, 31, 0, 0,
                                           tzinfo=tz.tzutc()))
