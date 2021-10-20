using UnityEngine;
using System.Collections.Generic;
using System.Collections;
using UnityEngine.SceneManagement;

// This is an audio visualizer. This will generate a circle using the amount of cubes and radius you specify.
// This script contains little to no comments.

public class SoundVisual : MonoBehaviour
{
   //public bool canDelete;
	private const int SAMPLE_SIZE = 1024;
   
	private float rmsValue;
	private float dbValue;
	private float pitchValue;

	public Material[] visualMaterial;

	public float visualModifier = 50.0f;
	public float smoothSpeed = 10.0f;
	public float maxVisualScale = 35.0f;
	public float keepPer = 0.5f;
	// public Vector3 Line;

	private AudioSource source;
	private float[] samples;
	private float[] spectrum;
	private float sampleRate;
    private GameObject cubes;
    public Transform Songmanager;

	private Transform[] visualList;
	private float[] visualScale;
	public int amnVisual = 64;

	void Start()
	{
       source = GetComponent<AudioSource>();
       samples = new float[SAMPLE_SIZE];
       spectrum = new float[SAMPLE_SIZE];
       sampleRate = AudioSettings.outputSampleRate;
       SpawnCircle();
    }

    private void amnVisualChange(int amn)
    {
        amnVisual = amn;
    }

    public void Delete()
    {
        Destroy(Songmanager.gameObject);
    }

    public void SpawnCircle()
    {
        
        visualScale = new float[amnVisual];
        visualList = new Transform[amnVisual];

        Vector3 center = Vector3.forward;
        float radius = 14.0f;

        for (int i = 0; i < amnVisual; i++)
        {
            float ang = i * 1.0f / amnVisual;
            ang = ang * Mathf.PI * 2;

            float x = center.x + Mathf.Cos(ang) * radius;
            float y = center.y + Mathf.Sin(ang) * radius;

            Vector3 pos = center + new Vector3(x, y, 0);
            cubes = GameObject.CreatePrimitive(PrimitiveType.Cube) as GameObject;
            cubes.transform.SetParent(Songmanager);
            cubes.transform.position = pos;
            cubes.transform.rotation = Quaternion.LookRotation(center, pos);
			cubes.GetComponent<Renderer>().materials = visualMaterial;
            visualList[i] = cubes.transform;
        }
    }

    void Update()
    {
        AnalyzeSound();
        UpdateVisual();
    }

	void UpdateVisual()
	{
		int visualIndex = 0;
		int spectrumIndex = 0;
		int averageSize = (int)(SAMPLE_SIZE * keepPer / amnVisual);
       
		while (visualIndex < amnVisual)
		{
			int j = 0;
            float sum = 0;

            if (visualList != null)
            {
                while (j < averageSize)
                {
                    sum += spectrum[spectrumIndex];
                    spectrumIndex++;
                    j++;
                }

                float scaleY = sum / averageSize * visualModifier;
                visualScale[visualIndex] -= Time.deltaTime * smoothSpeed;
                if (visualScale[visualIndex] < scaleY)
                {
                    visualScale[visualIndex] = scaleY;
                }

                if (visualScale[visualIndex] > maxVisualScale)
                {
                    visualScale[visualIndex] = maxVisualScale;
                }
                visualList[visualIndex].localScale = Vector3.one + Vector3.up * visualScale[visualIndex];
                visualIndex++;
            } else
            {
                return;
            }
		}
	}
	
	void AnalyzeSound()
	{
		source.GetOutputData(samples, 0);

		int i = 0;
		float sum = 0;
		for (; i < SAMPLE_SIZE; i++)
		{
			sum += samples[i] * samples[i];
		}
		rmsValue = Mathf.Sqrt(sum / SAMPLE_SIZE);


		dbValue = 20 * Mathf.Log10(rmsValue / 0.1f);

		source.GetSpectrumData(spectrum, 0, FFTWindow.BlackmanHarris);

		float maxV = 0;
		var maxN = 0;
		for(i = 0; i < SAMPLE_SIZE; i++)
		{
			if(!(spectrum[i] > maxV) && !(spectrum[i] > 0.0f))
				continue;

			maxV = spectrum[i];
			maxN = i;
		}
       
		float freqN = maxN;
		if(maxN > 0 && maxN < SAMPLE_SIZE - 1)
		{
			var dL = spectrum[maxN - 1] / spectrum[maxN];
			var dR = spectrum[maxN + 1] / spectrum[maxN];
			freqN += 0.5f * (dR * dR - dL * dL);
		}
		pitchValue = freqN * (sampleRate / 2) / SAMPLE_SIZE;
       
	}
}